#include <iostream>
#include <omp.h>

using namespace std;

void luSequential(float** mat, int size);

void luParallelFor(float** mat, int size);

void printMatrix(float** mat, int size);

int main() {
    int size = 3;
    
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