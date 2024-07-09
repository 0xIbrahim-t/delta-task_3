import socket
import mysql.connector
import threading

mydb = mysql.connector.connect(host="db", db="game_db", user="username", password="password")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 6000))
server_socket.listen()

def client(connection, address):
    print(f"{address} connected to the server")
    connected = True
    while connected:
        message = connection.recv(1024).decode("utf-8")
        mycursor = mydb.cursor()

        if message == "exit":
            connected = False
            mydb().close()
            break

        elif message.split(",")[0] == "login":
            mycursor = mydb.cursor()
            mycursor.execute('SELECT password FROM users WHERE username = %s', (message.split(",")[1],))
            password = mycursor.fetchone()
            if password is None:
                connection.send("incorrect".encode("utf-8"))
            else:
                connection.send(password[0].encode("utf-8"))
            mycursor.close()

        elif message.split(",")[0] == "signup":
            mycursor = mydb.cursor()
            mycursor.execute(f'SELECT username FROM users')
            usernames = mycursor.fetchall()
            usernames = [q[0] for q in usernames]
            if message.split(",")[1] in usernames:
                connection.send("username already exists".encode("utf-8"))
            else :
                mycursor.execute('INSERT INTO users (username, password, points) VALUES (%s, %s, %s)', (message.split(",")[1], message.split(",")[2], 0))
                mydb.commit()
                connection.send("Successfully signed up, you can now use that username and password to login to the game server!".encode("utf-8"))
            mycursor.close()
            
        elif message.split(",")[0] == "answer":
            mycursor = mydb.cursor()
            msg = ""
            mycursor.execute(f"SELECT question FROM QA where questionby != '{message.split(",")[1]}'")
            questions = mycursor.fetchall()

            for question in questions:
                mycursor.execute(f'SELECT answeredby FROM QA WHERE question = "{question[0]}"')
                answeredby = mycursor.fetchone()
                if answeredby is None:
                    answeredby = []
                else:
                    answeredby = answeredby[0].split(",")
                if message.split(",")[1] not in answeredby:
                    msg += question[0]
                    msg += "~"

            msg = msg[0:-1]
            connection.send(msg.encode("utf-8"))
            choice = connection.recv(1024).decode("utf-8")

            if choice.split(",")[0] == "correct":
                mycursor.execute(f'UPDATE users SET point = point + 1 WHERE username = "{message.split(",")[1]}"')

            mycursor.execute(f'SELECT answeredby FROM QA WHERE question = "{choice.split(",")[1]}"')
            updated = mycursor.fetchone()[0] + "," + message.split(",")[1]
            mycursor.execute(f'UPDATE QA SET answeredby = {updated} WHERE question = "{choice.split(",")[1]}"')
            mydb.commit()
            mycursor.close()

        elif message.split(",")[0] == "question":
            mycursor = mydb.cursor()
            QA = connection.recv(1024).decode("utf-8")
            mycursor.execute(f'INSERT INTO QA (question, questionby, answeredby) Values ("{QA}", "{message.split(",")[1]}", "")')
            mydb.commit()
            mycursor.close()

        elif message == "leaderboard":
            mycursor = mydb.cursor()
            leaderboard_msg = ""
            mycursor.execute("SELECT username FROM users ORDER BY points DESC")
            usernames_leaderboard = mycursor.fetchall()
            if usernames_leaderboard is None:
                leaderboard_msg = ""
            else:
                for username_leaderboard in usernames_leaderboard:
                    mycursor.execute(f'SELECT points FROM users WHERE username = "{username_leaderboard}"')
                    g = mycursor.fetchone()[0]
                    leaderboard_msg += username_leaderboard[0] + "," + str(g) + ";"
            connection.sendall(leaderboard_msg[0:-1].encode("utf-8"))
            mycursor.close()

    connection.close()
        

while True:
    connection, address = server_socket.accept()
    new_thread = threading.Thread(target=client, args=(connection, address))
    new_thread.start()
