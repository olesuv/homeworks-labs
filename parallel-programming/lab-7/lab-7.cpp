#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

double f_14(double x);

double trapezoidal_rule(double (*f)(double), double a, double b, int n);

double calculate_integral(double (*f)(double), double a, double b, int n, int rank, int size);

int main(int argc, char *argv[])
{
    int rank, size;
    double start_time, finish_time;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    double a = 5;
    double b = 10;
    int n = 10000;

    double result;

    start_time = MPI_Wtime();

    double local_result = calculate_integral(f_14, a, b, n, rank, size);

    MPI_Reduce(&local_result, &result, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    finish_time = MPI_Wtime();

    if (rank == 0)
    {
        printf("Trapezoidal rule result: %f\n", result);
        printf("Time: %f seconds\n", finish_time - start_time);
    }

    MPI_Finalize();

    return 0;
}

double f_14(double x)
{
    return log2(pow(x, 3));
}

double trapezoidal_rule(double (*f)(double), double a, double b, int n)
{
    double h = (b - a) / double(n);

    double *x = (double *)malloc((n + 1) * sizeof(double));
    double *y = (double *)malloc((n + 1) * sizeof(double));

    double area = 0;

    for (int i = 0; i <= n; i++)
    {
        x[i] = a + i * h;
        y[i] = f(x[i]);
    }

    for (int i = 1; i < n; i++)
    {
        area += y[i];
    }

    area += (y[0] + y[n]) / 2.0;
    area *= h;

    free(x);
    free(y);

    return area;
}

double calculate_integral(double (*f)(double), double a, double b, int n, int rank, int size)
{
    int local_n = n / size;
    int start = rank * local_n;
    int end = (rank + 1) * local_n - 1;

    if (rank == size - 1)
    {
        end = n - 1;
    }

    double local_result = trapezoidal_rule(f, a + start * (b - a) / n, a + end * (b - a) / n, end - start + 1);

    return local_result;
}
