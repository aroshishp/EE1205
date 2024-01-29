#include<stdio.h>
#include<math.h>

int main()
{
    //Generate n values from -6 to 6
    int n_values[13] = {0};
    for(int i = -6; i < 7; i++)
    {
        n_values[i+6] = i;
    }

    double x_values[13] = {0};
    //Set p = q = 0.5
    double q = 0.5;

    //Generate x_values using x = 2qnu(n)
    for(int i = 0; i < 13; i++)
    {
        x_values[i] =  (2 * q * fabs(n_values[i])) * (n_values[i] > 0);
    }

    // //Save n_values and x_values in nx_values.dat
    FILE *file = fopen("nx_values.dat", "w");
    if (file == NULL)
    {
        printf("Error opening file\n");
        return 1;
    }

    for (int i = 0; i < 13; i++)
    {
        fprintf(file, "%d  %.0f\n", n_values[i], x_values[i]);
    }

    fclose(file);
    return 0;
}
