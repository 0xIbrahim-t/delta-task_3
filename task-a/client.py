import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 6000))

connected = False

while True:
    print("Select an option below (enter 1 or 2): ")
    print("1. Login")
    print("2. Sign up")
    print("3. exit")
    message = input(">")
    if message == "1":
        username = input("Enter your username: ")
        password = input ("Enter your password: ")
        client.send(f"login,{username}".encode("utf-8"))
        passw = client.recv(1024).decode("utf-8")
        if password == passw:
            connected = True
            break
        else :
            print("Incorrect password!")

    elif message == "2":
        username = input("Enter your username(less than 10 char): ")
        password = input ("Enter your password: ")
        if len(username) < 10:
            client.send(f"signup,{username},{password}".encode("utf-8"))
            print(client.recv(1024).decode("utf-8"))
        else :
            print("should have username less than 10 characters")

    else:
        client.send("exit".encode("utf-8"))
        break

while connected:
    print("Select an option below (choose a number eg- enter 2): ")
    print("1. answer other players questions.")
    print("2. add a question")
    print("3. leaderboard")
    print("4. exit")
    choice = input(">")
#format = question_1~question_2 //// question_1 = question;a;b;c;d;correct
    if choice == 1:
        client.send(f"answer,{username}".encode("utf-8"))
        questions = client.recv(1024).decode("utf-8")
        question_answer = questions.split("~")

        y=0

        for i in question_answer.split(";")[0]:
            y += 1
            print(f"{y}. {i}")

        question_no = input("which question you wanna answer: ")
        print(f"Question : {question_answer.split(';')[0][question_no - 1]}")

        for v in range(1, 5):
            print(f"option {['a','b','c','d'][v - 1]} - {question_answer.split(";")[v]}")
            option = input("choose an option")
        
        if option == question_answer.split(";")[5] :
            client.send(f"correct,{question_answer}".encode("utf-8"))
            print("you answered it right!!!")
        
        else:
            client.send(f"wrong,{question_answer}".encode("utf-8"))
            print("sadly it was wrong :( tho")

    elif choice == 2:
        client.send(f"question,{username}".encode("utf-8"))
        add_question = input("enter the question(please do not use ~ or ; in the questions): ")
        option_a = input("enter option a: ")
        option_b = input("enter option b: ")
        option_c = input("enter option c: ")
        option_d = input("enter option d: ")
        correct_answer = input("enter the correct option (eg: a): ")
        client.send(f"{add_question};{option_a};{option_b};{option_c};{option_d};{correct_answer}".encode("utf-8"))
# players = name,points; name,points
    elif choice == 3:
        client.send("leaderboard".encode("utf-8"))
        full_info_players = ""
        while True:
            players = client.recv(1024)
            if len(players) == 0:
                break
            full_info_players += players.decode("utf-8")
        print("place  username  score")
        a = 0
        for player in players.split(";"):
            a += 1
            line = str(a) + " "*(7 - len(str(a))) + player[0] + " "*(10 - len(player[0])) + player[1]
            print(line)
    
    elif choice == 4:
        client.send("exit".encode("utf-8"))
        break
    else :
        print("Invalid choice!")
