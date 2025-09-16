#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if(argc>1){
        int doubleNumber(int number);
        int number = doubleNumber((atoi(argv[1])));
        printf("%d\n", number);}
    return 0;
}

int doubleNumber(int number) {
    return number<<1;
}