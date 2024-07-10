# Task-B


CTF challenges are cybersecurity competitions that test participants’ skills in various areas. These challenges simulate real-world scenarios and require participants to solve puzzles, find vulnerabilities, and exploit systems to uncover hidden flags. Flags are unique hidden pieces of information that serve as proof of a successful exploit or solution. CTF challenges provide an engaging and hands-on learning experience in cybersecurity.


### 1. Binary
Using the dangerous gets function, create a buffer overflow vulnerability in a binary file where you’ve to use buffer overflow to overwrite variables on the stack in order to get a hidden flag out of the binary file.
Use C to create and compile the program, turn off all the protections for the binary.
Create a Python script using the pwntools module to create a script that uses the vulnerability and fetches the flag.



### 2. Forensics
Using steganography techniques, hide any text file (encode the text inside in any form) inside this image: mystery.png.
Hint: look into the metadata for a clue related to steghide.



### 3. Web
Develop a simple web app using PHP and MySQL, including a login form that is intentionally susceptible to SQL injection.
Store a hidden flag in the database that is retrievable via this vulnerability.
Create a Python exploit script using the requests module to exploit this vulnerability, bypass the login, and retrieve the hidden flag from the database.
You need not focus much on the design of the website or its contents after the login page.
We encourage you to create and explore interesting SQL injections.



### 4. Reverse Engineering
Using some basic math and bit manipulation, make an obscure and obfuscated function that takes some string and calculates a value. The program should take any string as an input and use the function to calculate the value for the string, and will print out the flag only if it matches a hardcoded value in the program.
Using Z3 solver, reverse the function and find the secret string to see the flag.



### 5. Crypto
Write a simple Python script to implement RSA from scratch (crypto libraries are not allowed).
Take any input and encrypt and decrypt using your RSA implementation.
Sign another input using your private key and verify using public key.
You don't have to generate the prime numbers securely, you can use any prime numbers for your implementation.
