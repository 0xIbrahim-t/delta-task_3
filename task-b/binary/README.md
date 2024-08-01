## Binary
Using the dangerous gets function, create a buffer overflow vulnerability in a binary file where you’ve to use buffer overflow to overwrite variables on the stack in order to get a hidden flag out of the binary file.
Use C to create and compile the program, turn off all the protections for the binary.
Create a Python script using the pwntools module to create a script that uses the vulnerability and fetches the flag.


### to set up the environment
> pip install pwntools

### To get the hardcoded value which is in the string_to_value.c which is compiled to a binary file named string_to_value:
> python3 buffer_overflow.py

