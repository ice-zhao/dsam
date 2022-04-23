#include <stdio.h>
#include <stdlib.h>

char buffer[64];
char *path = "./test.txt";

int foo() {}

int main(int argc, char* argv[]){
    FILE *f = fopen(path, "r");
    if ( f == NULL ) {
        exit(0);
    }

    if (fgets(buffer, 64, f) == NULL)
        exit(0);

    foo();

    return 0;
}
