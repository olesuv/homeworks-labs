// Before building and starting project
// Follow this guide on configurating project:
// https://medium.com/geekculture/configuring-mpi-on-windows-10-and-executing-the-hello-world-program-in-visual-studio-code-2019-879776f6493f
#include <iostream>
#include <mpi.h>

using namespace std;

int main(int argc, char* argv[])
{
	int my_rank;
	int world_size;

	MPI_Init(NULL, NULL);

	MPI_Comm_size(MPI_COMM_WORLD, &world_size);
	MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

	cout << "Process: " << my_rank << " / " << world_size << endl;

	MPI_Finalize();
	
	return 0;
}