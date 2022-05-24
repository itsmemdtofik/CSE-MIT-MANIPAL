#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<mpi.h>

int main(int argc, char* argv[]){

	int myRank;
	int size;
	int N;
	int M;
	int i;
	int rootRank = 0;
	int sendBuffer[100];
	int recvdBuffer[100];
	float avgofEach = 0;
	float cBuffer[100];

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if(size != 4){
		printf("This application will run with 4 process : \n");
		MPI_Abort(MPI_COMM_WORLD, EXIT_FAILURE);
	}

	if(myRank == rootRank){
		N = size;
		printf("Enter the size : \n");
		scanf("%d", &M);
		printf("Enter the elements : \n");
		for(i = 0; i < N * M; i++){
			scanf("%d", &sendBuffer[i]);
		}
	}

	MPI_Bcast(&M, 1, MPI_INT, rootRank, MPI_COMM_WORLD);
	printf("I have recieved [ %d ] from the process [ %d] :\n", M, myRank);
	MPI_Scatter(&sendBuffer, M, MPI_INT, &recvdBuffer, M, MPI_INT, rootRank, MPI_COMM_WORLD);
	for(i = 0; i < M; ++i){
		avgofEach = avgofEach + recvdBuffer[i];
	}
	avgofEach = avgofEach / M;

	printf("The average are [ %.2f ] from process [%d]\n", avgofEach, myRank);
	MPI_Gather(&avgofEach, 1, MPI_FLOAT, &cBuffer, 1, MPI_FLOAT, rootRank, MPI_COMM_WORLD);

	if(myRank == rootRank){
		float totalAvg = 0;
			for(i = 0; i < N; i++)
				totalAvg = totalAvg + cBuffer[i];
		totalAvg = totalAvg / N;
		printf("The totalAvg is = %.2f\n", totalAvg);
	}

	MPI_Finalize();
	return 0;

}