#include<stdio.h>
#include<math.h>
#define POINTS 1000

double G_s(double s)
{
    return (3 * exp(-4 * s))/(12 * s + 1);
}

int main()
{
    FILE *fp;
    fp = fopen("assign9.dat", "w");
    if (fp == NULL)
    {
        printf("Error Opening File.\n");
        return 1;
    }

    for(double i = 0; i < 10; i += 0.001)
    {
        double G_val = G_s(i);
        fprintf(fp, "%f   %f\n", i, G_val);
    }

    fclose(fp);
    return 0;
}