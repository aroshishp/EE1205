#include <stdio.h>
#include <math.h>

void decimalToHexadecimal(int decimalNumber) {
    int quotient;
    int i = 1;
    char hexadecimalNumber[100];

    quotient = decimalNumber;

    while (quotient != 0) {
        int remainder = quotient % 16;

        // Convert remainder to hexadecimal
        if (remainder < 10)
            hexadecimalNumber[i++] = 48 + remainder;
        else
            hexadecimalNumber[i++] = 55 + remainder;

        quotient = quotient / 16;
    }

    // Print hexadecimal number in reverse order
    printf("Hexadecimal equivalent of %d is: ", decimalNumber);
    for (int j = i - 1; j > 0; j--)
        printf("%c", hexadecimalNumber[j]);
    	puts("");
}

int main() {
    FILE *file = fopen("assign3.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
//Generate V_in and V_out values	
    for (int i = 0; i < 10000; i++) {
        double V_in = i / 100.0;
        double V_out = floor((V_in + 9.8) / 19.6);
        fprintf(file, "%.2f %.0f\n", V_in, V_out);
    }

    fclose(file);

    double given_V_in = 1.9922;
    double V_min = 0.0;
    double V_max = 5.0;
    double bits = 8.0;

    double req_V_out_10 = given_V_in * (pow(2, bits) - 1) / (V_max - V_min);

    decimalToHexadecimal(round(req_V_out_10));

//Using format specifier
    //int V_out_approx = round(req_V_out_10);
    //printf("\nHexadecimal Output: %X\n", V_out_approx);
    return 0;
}
