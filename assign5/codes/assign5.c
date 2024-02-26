#include <stdio.h>
#include <math.h>

#define NUM_POINTS 1000

double V_out(double omega, double C) {
    double numerator = 5 * sqrt(1 + 100 * pow(omega, 2) * pow(C, 2));
    double denominator = sqrt(1 + 121 * pow(omega, 2) * pow(C, 2));
    double phase_angle = -atan(omega * C / (1 + 110 * pow(omega, 2) * pow(C, 2)));
    return numerator * cos(phase_angle) / denominator;
}

int main() {
    FILE *fp;
    fp = fopen("assign5.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    double omega;
    double C = 1.0;  // Adjust C value if needed

    for (int i = 0; i < NUM_POINTS; ++i) {
        omega = 10.0 * i / (NUM_POINTS - 1);
        double V_out_value = V_out(omega, C);
        fprintf(fp, "%.6lf %.6lf\n", omega, V_out_value);
    }

    fclose(fp);
    printf("Data saved to assign5.dat\n");

    return 0;
}
