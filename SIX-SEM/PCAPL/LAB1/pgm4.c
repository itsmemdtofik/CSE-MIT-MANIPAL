#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char *argv[])
{
    int myRank;
    int size;
    char str[100] = "HeLLO";
    char ch;
    size = strlen(str);
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    for(int i = 0; i <= strlen(str); i++){
        if(i == myRank){

            ch = str[i];
            
            if(ch >= 'A' && ch <= 'Z'){
                ch = ch + 32;
                printf("The rank is = [ %d ] and character is = [ %c ]", i, ch);
            }else if(ch >= 'a' && ch <= 'z'){
                ch = ch - 32;
                printf("The rank is = [ %d ] and character is = [ %c ]", i, ch);
            }
            str[i] = ch;
        }
    }
    MPI_Finalize();
    return 0;
}