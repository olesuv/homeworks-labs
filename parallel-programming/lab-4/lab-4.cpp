#include <iostream>
#include <omp.h>


using namespace std;


void luSequential(float** mat, int size);

void luParallelFor(float** mat, int size);

void luParallelTask(float** mat, int size);


void printMatrix(float** mat, int size);

float** createRandomMatrix(int size, float minVal, float maxVal);

void deleteMatrix(float** mat, int size);


int main() {
    int AMOUNT = 0;

    float minVal = 0, maxVal = 0;

    cout << "Enter amount of elements in matrix: ";
    cin >> AMOUNT;

    cout << "Enter minimum value: ";
    cin >> minVal;

    cout << "Enter maximum value: ";
    cin >> maxVal;

    srand(time(NULL)); // Seed random number generator

    float** mat1 = createRandomMatrix(AMOUNT, minVal, maxVal);

    cout << "Sequential LU" << endl;
    luSequential(mat1, AMOUNT);
    printMatrix(mat1, AMOUNT);

    cout << "Parallel For LU" << endl;
    luParallelFor(mat1, AMOUNT);
    printMatrix(mat1, AMOUNT);

    cout << "Parallel Task LU" << endl;
    luParallelTask(mat1, AMOUNT);
    printMatrix(mat1, AMOUNT);

    deleteMatrix(mat1, AMOUNT);

    return 0;
}



void luSequential(float** mat, int size) {
    for (int k = 0; k < size; k++) {
        for (int i = k + 1; i < size; i++) {
            mat[i][k] = mat[i][k] / mat[k][k];
            for (int j = k + 1; j < size; j++) {
                mat[i][j] = mat[i][j] - mat[i][k] * mat[k][j];
            }
        }
    }
}

void luParallelFor(float** mat, int size) {
    for (int k = 0; k < size; k++) {
#pragma omp parallel for
        for (int i = k + 1; i < size; i++) {
            mat[i][k] = mat[i][k] / mat[k][k];
            for (int j = k + 1; j < size; j++) {
                mat[i][j] = mat[i][j] - mat[i][k] * mat[k][j];
            }
        }
    }
}

void luParallelTask(float** mat, int size) {
    for (int k = 0; k < size; k++) {
#pragma omp parallel
        {
#pragma omp single
            {
                for (int i = k + 1; i < size; i++) {
                    mat[i][k] = mat[i][k] / mat[k][k];
#pragma omp task
                    {
                        for (int j = k + 1; j < size; j++) {
                            mat[i][j] = mat[i][j] - mat[i][k] * mat[k][j];
                        }
                    }
                }
            }
        }
    }
}

void printMatrix(float** mat, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

float** createRandomMatrix(int size, float minVal, float maxVal) {
    float** mat = new float* [size];
    for (int i = 0; i < size; i++) {
        mat[i] = new float[size];
        for (int j = 0; j < size; j++) {
            mat[i][j] = minVal + static_cast<float>(rand()) / static_cast<float>(RAND_MAX / (maxVal - minVal));
        }
    }
    return mat;
}

void deleteMatrix(float** mat, int size) {
    for (int i = 0; i < size; i++) {
        delete[] mat[i];
    }
    delete[] mat;
}
