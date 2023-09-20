// For Windows users:
// Before building and starting project
// Follow this guide on configurating project:
// https://medium.com/geekculture/configuring-mpi-on-windows-10-and-executing-the-hello-world-program-in-visual-studio-code-2019-879776f6493f
#include <iostream>
#include <vector>
#include <ctime>
#include <mpi.h>

using namespace std;

int main(int argc, char** argv)
{
    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    srand(time(NULL) + rank);

    const int vector_size = 5;

    vector<int> vector(vector_size);

    if (rank == 0)
    {
        // процес A
        for (int i = 0; i < vector_size; i++)
        {
            vector[i] = rand() % 10;
        }

        cout << "Process " << rank << " generated the following vector: ";

        for (int i = 0; i < vector_size; i++)
        {
            cout << vector[i] << " ";
        }
        cout << endl;

        MPI_Send(vector.data(), vector_size, MPI_INT, 1, 0, MPI_COMM_WORLD);

        cout << "Process " << rank << " sent the vector to process 1" << endl;

        MPI_Recv(vector.data(), vector_size, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

        cout << "Process " << rank << " received the modified vector from process 1: ";

        for (int i = 0; i < vector_size; i++)
        {
            cout << vector[i] << " ";
        }

        cout << endl;
    }

    else if (rank == 1)
    {
        // процес B
        MPI_Recv(vector.data(), vector_size, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

        cout << "Process " << rank << " received the following vector from process 0: ";

        for (int i = 0; i < vector_size; i++)
        {
            cout << vector[i] << " ";
        }
        cout << endl;

        const int x = 2;

        for (int i = 0; i < vector_size; i++)
        {
            vector[i] *= x;
        }

        MPI_Send(vector.data(), vector_size, MPI_INT, 0, 0, MPI_COMM_WORLD);

        cout << "Process " << rank << " sent the modified vector to process 0" << endl;
    }

    MPI_Finalize();

    return 0;
}
