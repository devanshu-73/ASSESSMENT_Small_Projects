#include <stdio.h>
void Multi();
int main()
{

    Multi();
    return 0;
}
void Multi()
{
    int a[4][4], b[4][4], c[4][4];
    printf("Matrix Multiplication \n");
    printf("------- Enter Matrix : 1 -------\n\n");
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }
    // for(int i=0; i<4; i++)
    // {
    //     for(int j=0; j<4; j++)
    //     {
    //         printf("%d",a[i][j]);
    //     }
    //     printf("\n");
    // }

    printf("------- Enter Matrix : 2 -------\n\n");
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            scanf("%d", &b[i][j]);
        }
    }
    // for(int i=0; i<4; i++)
    // {
    //     for(int j=0; j<4; j++)
    //     {
    //         printf("%d",b[i][j]);
    //     }
    //     printf("\n");
    // }

    printf("\n Multiplication :\n");

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            c[i][j] = 0;
            for (int k = 0; k < 4; k++)
            {
                c[i][j] = c[i][j] + a[i][k] * b[k][j];
            }
        }
    }
     printf("\n The Result is .....\n");
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }
}
