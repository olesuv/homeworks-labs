#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

#define ROWS 3
#define COLS 3

int main(int argc, char** argv) {
    int rank, size;
    int matrix[ROWS][COLS];
    int local_max[ROWS];
    int global_max[ROWS];
    int local_sum = 0;
    int global_sum = 0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Initialize the matrix with random values
    srand(rank);
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            matrix[i][j] = rand() % 100;
        }
    }

    // Find the local maximum element in each row
    for (int i = 0; i < ROWS; i++) {
        local_max[i] = matrix[i][0];
        for (int j = 1; j < COLS; j++) {
            if (matrix[i][j] > local_max[i]) {
                local_max[i] = matrix[i][j];
            }
        }
    }

    // Compute the local sum of the maximum elements
    for (int i = 0; i < ROWS; i++) {
        local_sum += local_max[i];
    }

    MPI_Reduce(&local_sum, &global_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        printf("Matrix:\n");
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                printf("%d ", matrix[i][j]);
            }
            printf("\n");
        }

        printf("Sum of the maximum elements in the rows of the matrix with %d amount of processes: %d\n", size, global_sum);
    }

    MPI_Finalize();

    return 0;
}
