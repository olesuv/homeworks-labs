#include <iostream>
#include <omp.h>

using namespace std;

int main()
{
	int amount = 0;

	cout << "Type number of threads: ";
	cin >> amount;

#pragma omp parallel num_threads(amount)
	{
		int t_id = omp_get_thread_num();
		int t_amount = omp_get_num_threads();
		int p_amount = omp_get_num_procs();

		cout << "Amount of processors: " << p_amount << endl;
		cout << "I am " << t_id << " thread from " << t_amount << " threads!" << endl;
	}

	int start_value = 0;

#pragma omp parallel num_threads(amount) private(start_value)
	{
		start_value += 1;
		cout << "Private thread. Value: " << start_value << endl;
	}

	cout << "Original start value after private: " << start_value << endl;

#pragma omp parallel shared(start_value)
	{
		start_value += 1;
	}

	cout << "Original start value after shared: " << start_value << endl;

#pragma omp parallel num_threads(2)
	{
		int n = omp_get_thread_num();
#pragma omp sections
		{
#pragma omp section
			{
				cout << "First section, process " << n << endl;
			}
#pragma omp section
			{
				cout << "Second section, process " << n << endl;
			}
		}
		cout << "Parallel section, process " << n << endl;
	}
}
