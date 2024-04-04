#include <stdio.h>
#include<math.h>
#define N 10

int main() {
    double hn1[N + 2] = {0};
    double hn2[N + 2] = {0};

    // Pad hn1 with two zeros at the end
    for (int i = 0; i < N; ++i) {
        hn1[i] = pow(-1.0 / 2, i);
    }

    // Pad hn2 with two zeros at the beginning
    for (int i = 0; i < N; ++i) {
        hn2[i + 2] = hn1[i];
    }

    // Save data to file
    FILE *fp;
    fp = fopen("5.2.dat", "w");
    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    for (int i = 0; i < N + 2; ++i) {
        fprintf(fp, "%d %f\n", i, hn1[i] + hn2[i]);
    }
    fclose(fp);

    return 0;
}
