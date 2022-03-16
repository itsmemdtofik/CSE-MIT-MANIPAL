#include<stdio.h>
#include<mpi.h>

int main(int argc, char* argv[]){

	int myRank;
	int size;
	int sendNumber;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status myStatus;

	if(myRank == 0){
		printf("Enter the number : \n");
		scanf("%d", &sendNumber);
		MPI_Send(&sendNumber, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
		MPI_Recv(&sendNumber, 1, MPI_INT, (size - 1), 1, MPI_COMM_WORLD, &myStatus);
		fprintf(stdout, "Process received number [ %d ] in process [ %d ] from process [ %d ]\n", sendNumber, myRank, (size - 1));

	}else{
		MPI_Recv(&sendNumber, 1, MPI_INT, (myRank - 1), 1, MPI_COMM_WORLD, &myStatus);
		fprintf(stdout, "Process received number [ %d ] in process [ %d ] from process [ %d ]\n", sendNumber, myRank, (myRank - 1));
		sendNumber = sendNumber + 1;

		MPI_Send(&sendNumber, 1, MPI_INT, (myRank + 1) % size, 1, MPI_COMM_WORLD);
	}
	MPI_Finalize();
	return 0;
}