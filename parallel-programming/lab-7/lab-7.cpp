// Before building and starting project
// Follow this guide on configurating project:
// https://medium.com/geekculture/configuring-mpi-on-windows-10-and-executing-the-hello-world-program-in-visual-studio-code-2019-879776f6493f

#include <iostream>
#include <mpi.h>

using namespace std;

double f_14(double x);

double trapezoidal_rule(double (*f)(double), double a, double b, int n);

double calculate_integral(double (*f)(double), double a, double b, int n, int rank, int size);

int main(int argc, char *argv[])
{
	int rank, size;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	double a = 5;
	double b = 10;
	int n = 10000;

	double result;

	double local_result = calculate_integral(f_14, a, b, n, rank, size);

	MPI_Reduce(&local_result, &result, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

	if (rank == 0)
	{
		cout << "Trapezoidal rule result: " << result << endl;
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

	double *x = new double[n + 1];
	double *y = new double[n + 1];

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

	delete[] x;
	delete[] y;

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
