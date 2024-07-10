from random import randint
from math import gcd

def check_not_prime_num(a):
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0 or a % 7 == 0 or a % 11 == 0:
        return True
    
    for i in range(3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return True  
    return False

def generate_prime_nums(min, max):
    a = randint(min, max)
    b = randint(min, max)

    while check_not_prime_num(a):
        a = randint(min, max)
    while check_not_prime_num(b) or a == b: 
        b = randint(min, max)
    return (a, b)

def mod_exp(a, b, c):
    end_ans = 1
    while b > 0:
        if b % 2 == 1:
            b -= 1
            end_ans = (end_ans * a) % c
        b = b // 2 
        a = (a * a) % c
    return end_ans % c

run = True

while run:
    print("1. create public and private key pair")
    print("2. encrypt a message")
    print("3. decrypt a message")
    print("4. Sign a message")
    print("5. verify a message")
    choice = input("choose a option and enter a number: ")

    if choice == "1":
        prime_nums = generate_prime_nums(100, 9999)

        n = prime_nums[0] * prime_nums[1]
        phi_n = (prime_nums[0] - 1) * (prime_nums[1] - 1)

        while True:
            public_key = randint(2, phi_n - 1)
            if gcd(public_key, phi_n) == 1:
                break

        private_key = int(phi_n/public_key)

        while True:
            private_key += 1
            if (public_key * private_key) % phi_n == 1:
                break 
        print(f"your public key pair : {(public_key, n)}")
        print(f"your private key pair : {(private_key, n)}")


    elif choice == "2":
        encrypted_message = []
        publicKey = eval(input("enter the publicKey in the format (a, b): "))
        message = input("Enter your message which you want to encrypt: ")
        for letter in message:
            encrypted_message += [mod_exp(ord(letter), publicKey[0], publicKey[1])]
        print("here is your encrypted message", encrypted_message)


    elif choice == "3":
        decrypted_message = ""
        privateKey = eval(input("enter your private key in the format (a, b): "))
        message = eval(input("Enter your encrypted message which you want decrypt: "))
        for letter in message:
            decrypted_message += chr(mod_exp(letter, privateKey[0], privateKey[1]))
        print("here is your decrypted message", decrypted_message)

    elif choice == "4":
        signature = []
        privateKey = eval(input("enter your private key in the format (a, b): "))
        message = input("Enter your message which you want sign: ")
        for letter in message:
            signature += [mod_exp(ord(letter), privateKey[0],  privateKey[1])]
        print("here is your signature for the message", signature)

    elif choice == "5":
        verifying_message = ""
        publicKey = eval(input("enter the publicKey in the format (a, b): "))
        message_to_verify = input("Enter the message which you want to verify: ")
        signature = eval(input("Enter the signature which you want to verify with: "))
        for letter in signature:
            verifying_message += chr(mod_exp(letter, publicKey[0], publicKey[1]))
        if verifying_message == message_to_verify:
            print("Message verified!, signature and message matched successfully")
        else:
            print("The signature and message did not match.")

    else:
        print("invalid choice")
