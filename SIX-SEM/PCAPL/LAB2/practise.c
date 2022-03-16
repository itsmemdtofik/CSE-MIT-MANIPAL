#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[])
{

    int myRank;
    int size;
    int x;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;

    if (myRank == 0)
    {
        printf("Please Enter a value in Master Process : \n");
        scanf("%d", &x);
        MPI_Send(&x, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
        fprintf(stdout, "I have sent %d from process 0\n", x);
        fflush(stdout);
    }
    else
    {
        MPI_Recv(&x, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
        fprintf(stdout, "I have recieved %d in process 1 \n", x);
        fflush(stdout);
    }
    MPI_Finalize();
    return 0;
}