#include <stdio.h>
#include <math.h>

// Define constants
#define T 0.001    // Time period of square waveform
#define tau 0.00005    // Time constant of RC circuit

// Define square waveform function
double square_wave(double t) {
    return (2*(2*floor((t-T/4)/T) - floor(2*(t-T/4)/T)) + 1) * (t > T/4);
}

// Define RC circuit response function
double rc_response(double t) {
    double t_adjusted = t - (2 * floor(2 * t / T + 0.5) - 1) * T/4;
    return exp(-(t_adjusted / tau)) * square_wave(t);
}

int main() {
    FILE *fp;
    double t, V_out;

    // Open file for writing
    fp = fopen("rc_data.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate and save data
    for (t = 0; t <= 5*T/2; t += 5*T/2 / 10000) {
        V_out = rc_response(t);
        fprintf(fp, "%lf %lf\n", t, V_out);
    }

    // Close file
    fclose(fp);

    return 0;
}
