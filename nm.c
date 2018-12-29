#include <stdio.h>
#include <stdlib.h>
//#include <conio.h>

#define MAX 100

void printout(int aa[MAX+1][MAX+1], int max)
{
  int i, j;
  printf("From 2 - %d:\n", max);
  for (i=2; i<=max; i++)
    for (j=i; j<=max; j++)
      if (aa[i][j])
        printf("i=%d, j=%d\n", i, j);
  // _getch();
}


int main(int argn, char* argv[])
{
  int i,j,m,n,flag,max;
  int aa[MAX+1][MAX+1];
  
  if (argn>1)
    max = atoi(argv[1]);
  if (max<10 || max >MAX)
    max = MAX;

  for (i=2; i<=max; i++)	// Create all possible productions 
    for(j=i; j<=max; j++)
      aa[i][j] = i*j;

  if (argn>3)
    printout(aa, max);

  for (i=2; i<=max; i++) 	// Filter out the unique product
    for (j=i; j<=max; j++)
      {
        flag = 1;
        for (m=2; m<=max && flag; m++)
          for (n=m; n<=max && flag; n++)
            if (aa[i][j]==aa[m][n] && i!=m && j!=n)
              flag = 0;
        if(flag)
          aa[i][j] = 0;
      }
  
  if (argn>2)
    printout(aa, max);
 
  for (i=2; i<=max; i++) 	// Filter out the identical sum
    for (j=i; j<=max; j++)
      {
        flag = 0;
        if (aa[i][j])
          {
             for(m=i; m<=max; m++)
               for(n=(i==m?j+1:m); n<=max; n++)
                 if (aa[m][n] && ((i+j)==(m+n)))
                   {
                      aa[m][n] = 0;
                      flag = 1;
                   }
             if (flag)
               aa[i][j]=0;
          }
      }
  if (argn>2)
    printout(aa, max);

  for (i=2; i<=max; i++) 	// Filter out the identical product
    for (j=i; j<=max; j++)
      {
        flag = 0;
        if (aa[i][j])
          {
            for (m=i; m<=max; m++)
              for (n=(i==m?j+1:m); n<=max; n++)
                if (aa[m][n] == aa[i][j])
                  {
                    aa[m][n] = 0;
                    flag = 1;
                  }
            if (flag)
              aa[i][j] = 0;
          }
      }
  printout(aa,max);
  return(0);
}
