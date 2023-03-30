#include <iostream>
#include <omp.h>


using namespace std;

void print_arr(double* a, int n);
void create_random_arr(double* a, int n);

void bubble_sort(double* a, int n);
void bubble_parallel_sort(double* a, int n);

void oddevensort(double* a, int n);
void oddevensort_paralell(double* a, int n);


int main()
{
	int arr_size = 0;

	double* arr = NULL;
	double* arr_1 = NULL;
	double* arr_2 = NULL;
	double* arr_3 = NULL;

	cout << "Enter array size: ";
	cin >> arr_size;

	arr = new double[arr_size];
	arr_1 = new double[arr_size];
	arr_2 = new double[arr_size];
	arr_3 = new double[arr_size];


	create_random_arr(arr, arr_size);
	create_random_arr(arr_1, arr_size);
	create_random_arr(arr_2, arr_size);
	create_random_arr(arr_3, arr_size);


	double start = omp_get_wtime();

	bubble_sort(arr, arr_size);

	double end = omp_get_wtime();

	double time = end - start;

	cout << "Time of single bubble sort: " << time;
	//cout << endl;
	//print_arr(arr, arr_size);


	start = omp_get_wtime();

	bubble_parallel_sort(arr_1, arr_size);

	end = omp_get_wtime();

	time = end - start;

	cout << "\nTime of parallel bubble sort: " << time;
	//cout << endl;
	//print_arr(arr_1, arr_size);


	double start_2 = omp_get_wtime();

	oddevensort(arr_2, arr_size);

	double end_2 = omp_get_wtime();

	double time_2 = end_2 - start_2;

	cout << "\nTime of odeven sort: " << time_2;
	//cout << endl;
	//print_arr(arr_2, arr_size);


	double start_3 = omp_get_wtime();

	oddevensort_paralell(arr_3, arr_size);

	double end_3 = omp_get_wtime();

	double time_3 = end_3 - start_3;

	cout << "\nTime of parallel odeven sort: " << time_3;
	//cout << endl;
	//print_arr(arr_3, arr_size);


	return 0;
}

void print_arr(double* a, int n)
{
	for (int i = 0; i < n; i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;
}

void create_random_arr(double* a, int n)
{
	srand(time(NULL));

	for (int i = 0; i < n; i++) {
		a[i] = (double)rand() / RAND_MAX;
	}
}

void bubble_sort(double* a, int n)
{
	double t = 0;

	for (int i = 0; i < n - 1; i++)
	{
		for (int j = 0; j < n - i; j++)
		{
			if (a[j - 1] > a[j])
			{
				t = a[j];
				a[j] = a[j - 1];
				a[j - 1] = t;
			}
		}
	}
}

void bubble_parallel_sort(double* a, int n)
{
	double t = 0;

#pragma omp parallel shared(a, n) private(t)
	{
#pragma omp for collapse(2)
		for (int i = 0; i < n - 1; i++)
		{
			for (int j = 0; j < n - i - 1; j++)
			{
				if (a[j] > a[j + 1])
				{
					t = a[j];
					a[j] = a[j + 1];
					a[j + 1] = t;
				}
			}
		}
	}
}

void oddevensort(double* a, int n)
{
	double t = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = (i % 2) ? 0 : 1; j < n - 1; j += 2)
		{
			if (a[j] > a[j + 1])
			{
				t = a[j + 1];
				a[j + 1] = a[j];
				a[j] = t;
			}
		}
	}
}


void oddevensort_paralell(double* a, int n)
{
	double t = 0;

#pragma omp parallel shared(a, n) private(t)
	{

#pragma omp for collapse(2)
		for (int i = 0; i < n; i++)
		{
			for (int j = (i % 2) ? 0 : 1; j < n - 1; j += 2)
			{
				if (a[j] > a[j + 1])
				{
					t = a[j + 1];
					a[j + 1] = a[j];
					a[j] = t;
				}
			}
		}

	}
}
