#include <iostream>
#include <omp.h>

using namespace std;

double using_atomic(double result, double temp, double x, int N);

double using_locks(double result, double temp, double x, int N);

int main()
{
    double result = 0;
    double temp = 0;
    double x = 0;
    int N = 10000;

    int choice = -5;

    while (choice != 0)
    {
        cout << "1 - Using atomic" << endl;
        cout << "2 - Using locks" << endl;
        cout << "0 - Exit" << endl;

        cout << "Your choice: ";

        cin >> choice;

        switch (choice)
        {
        case 1:
            result = using_atomic(result, temp, x, N);

            cout << "ln(1 + " << x << ") = " << result << endl << endl;

            break;

        case 2:
            result = using_locks(result, temp, x, N);

            cout << "ln(1 + " << x << ") = " << result << endl << endl; 

            break;

        default:
            break;
        }
    }
    
    return 0;
}

double using_atomic(double result, double temp, double x, int N)
{
#pragma omp parallel for private(x)
    for (int n = 1; n <= N; n++)
    {
        temp = (pow(-1, n + 1) * pow(x, n)) / n;

#pragma omp atomic
        result += temp;
    }

    return result;
}

double using_locks(double result, double temp, double x, int N)
{
    omp_lock_t lock;

    omp_init_lock(&lock);

#pragma omp parallel for private(temp)
    for (int n = 1; n <= N; n++)
    {
        temp = (pow(-1, n + 1) * pow(x, n)) / n;

        omp_set_lock(&lock);
        result += temp;
        omp_unset_lock(&lock);
    }

    return result;

    omp_destroy_lock(&lock);
}
