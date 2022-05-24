#include"mpi.h"
#include<stdio.h>
#include<string.h>

int main(int argc,char *argv[])
{
	int rank,size,N,len,i,B[10],j;
    char str[20],rcv[10];
    int flag=0;
    int part,count=0;
    char v[5]={'a','e','i','o','u'};
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&N);

    if(rank==0)
    {
       fprintf(stdout,"enter a string :\n");
       fflush(stdout);
       scanf("%s",str);
       len=strlen(str);
       part=len/N;

   }
   MPI_Bcast(&part,1,MPI_INT,0,MPI_COMM_WORLD);
   MPI_Scatter(str,part,MPI_CHAR,rcv,part,MPI_CHAR,0,MPI_COMM_WORLD);
   fprintf(stdout,"i have recieved %s process %d\n",rcv,rank);
   fflush(stdout);
   for(i=0;i<part;i++)
   {
    flag=0;
    for(j=0;j<5;j++)
        if(rcv[i]==v[j])
            flag=1;
        if(flag==0)
            count++;
    }
    MPI_Gather(&count,1,MPI_INT,B,1,MPI_INT,0,MPI_COMM_WORLD);
    if(rank==0)
    {
        int sum=0;
        fprintf(stdout,"the result gathered in the root\n");
        fflush(stdout);
        for(i=0;i<N;i++)
        {
            fprintf(stdout,"%d\t",B[i]);
            sum=sum+B[i];

        }
        fprintf(stdout,"\nthe result in the root is %d\n",sum);
        fflush(stdout);

    }
    MPI_Finalize();
    return 0;
}