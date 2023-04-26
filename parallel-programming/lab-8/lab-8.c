#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

#define MATRIX_SIZE 3

int main(int argc, char** argv) {
    int rank, size;
    int matrix[MATRIX_SIZE][MATRIX_SIZE];
    int row_max[MATRIX_SIZE], row_sum = 0;
    double time_start = 0, time_finish = 0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Fill the matrix with random values
    for (int i = 0; i < MATRIX_SIZE; i++) {
        for (int j = 0; j < MATRIX_SIZE; j++) {
            matrix[i][j] = rand() % 100;
        }
    }

    // Find the maximum value in each row
    for (int i = 0; i < MATRIX_SIZE; i++) {
        int max = 0;
        for (int j = 0; j < MATRIX_SIZE; j++) {
            if (matrix[i][j] > max) {
                max = matrix[i][j];
            }
        }
        row_max[i] = max;
    }

    MPI_Barrier(MPI_COMM_WORLD);

    time_start = MPI_Wtime();
    MPI_Reduce(row_max, &row_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    time_finish = MPI_Wtime() - time_start;

    if (rank == 0) {
        for (int i = 0; i < MATRIX_SIZE; i++) {
            for (int j = 0; j < MATRIX_SIZE; j++) {
                printf("%d ", matrix[i][j]);
            }
            printf("\n");
        }

        printf("Sum of maximum values: %d\n", row_sum);
        printf("Reduce time: %f\n", time_finish);
    }

    MPI_Finalize();

    return 0;
}
