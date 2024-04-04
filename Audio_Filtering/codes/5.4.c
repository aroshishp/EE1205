#include <stdio.h>

#define K 12

int main() {
    double h[K] = {0};

    // Initial parameters
    h[0] = 1;
    h[1] = -0.5 * h[0];
    h[2] = -0.5 * h[1] + 1;

    // Recursive Relation
    for (int n = 3; n < K - 1; ++n) {
        h[n] = -0.5 * h[n - 1];
    }

    FILE *fp;
    fp = fopen("5.4.dat", "w");
    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    for (int i = 0; i < K; ++i) {
        fprintf(fp, "%d %f\n", i, h[i]);
    }
    fclose(fp);

    return 0;
}
