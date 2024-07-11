#include <stdio.h>
#include <string.h>

int string_to_value(char string[]){
    int sum = 0;
    for (int i = 0; i < strlen(string); i++) {
        sum += (int)string[i];
    }
    return strlen(string) * sum;
}

int main(int argc, char* argv[]){
    int flag_int = 1640;
    if (string_to_value(argv[1]) == flag_int) {
        printf("%d, You have the found the flag", string_to_value(argv[1]));
    }
    else {
        printf("%d", string_to_value(argv[1]));
    }
    return 0;
}
