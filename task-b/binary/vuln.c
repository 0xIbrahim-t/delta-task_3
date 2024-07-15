#include <stdio.h>

void flag(){
    printf("\nYou have found the flag \n");
}

void name(){
    char buffer[20];
    printf("what do you want:");
    gets(buffer);
}

int main(){
    name();
    return 0;
}
