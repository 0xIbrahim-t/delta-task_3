## Reverse Engineering
Using some basic math and bit manipulation, make an obscure and obfuscated function that takes some string and calculates a value. The program should take any string as an input and use the function to calculate the value for the string, and will print out the flag only if it matches a hardcoded value in the program.
Using Z3 solver, reverse the function and find the secret string to see the flag.

#### The string_to_value.c file has the functions which takes a string line in command line arguments and convert it to a certain value

#### the hardcoded value is 1640 and the secret string is flag


### To get the hardcoded value which is in the string_to_value.c which is compiled to a binary file named string_to_value:
> python3 reverse_engineering.py
