#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char* argv[]) {
    if(argc == 1) {
        printf("No argument provided\n");
        return 1; }
    float number = atof(argv[1]);
    int int_number = (int)number;
    if(number != int_number) {
        printf("Input is not an integer, not calculating factorial\n");
    }
    else {
        if(int_number < 0) {
            printf("Number is negative, not calculating factorial\n");
        }
        else {
            printf("Calculating x!\n");
            if(int_number == 0){printf("x! is 1\n");}
            else{
                int answer = 1;
                for(int i = int_number; i > 1; i-=1){
                    answer *= i;
                }
                printf("x! is %d\n", answer);
            }
        }
    }
    printf("Calculating e^x\n");
    float exp_answer = expf(number);
    printf("e^x is %f\n", exp_answer);

    printf("Calculating ln(x)\n");
    float ln_answer = logf(number);
    printf("ln(x) is %f\n", ln_answer);

    printf("Exiting\n");

    return 0;
}