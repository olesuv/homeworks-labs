#include <iostream>
#include <omp.h>
#include <vector>

using namespace std;

int main()
{
	int max_val = 0;
	int SIZE = 0;
	vector<int> random_vector = {};

	cout << "Enter vector size: ";
	cin >> SIZE;

#pragma parallel for
	for (int i = 0; i < SIZE; i++)
	{
		random_vector.push_back(rand() % 100);
	}

#pragma parallel for
	for (int i = 0; i < SIZE; i++)
	{
		cout << random_vector[i] << " ";
	}

	cout << endl;

	double start_time = omp_get_wtime();

#pragma parallel for reduction(max : max_val) schedule(dynamic)
	for (int i = 0; i < SIZE; i++)
	{
		cout << "[" << omp_get_thread_num() << "]: calculation of the iteration number " << i << endl;

		if (random_vector[i] >= max_val) 
		{
			max_val = random_vector[i];
		}
	}

	double end_time = omp_get_wtime();

	double thread_time = end_time - start_time;

	cout << "Max value of vector: " << max_val << endl;
	cout << "Time: " << thread_time << endl;

	random_vector.clear();

	return 0;
}
