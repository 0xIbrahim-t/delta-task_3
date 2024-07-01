import socket
import mysql.connector
import threading

mydb = mysql.connector.connect(host="db", db="game_db", user="username", password="password")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname())), 6000)
server_socket.listen()

def client(connection, address):
    print(f"{address} connected to the server")
    connected = True
    while connected:
        message = connection.recv(1024).decode("utf-8")
        if message == "Leave game":
            connected = False
            mycursor.close()
            break
        else :
            mycursor = mydb.cursor()
            mycursor.execute(message)
            mydb.commit()
    connection.close()
        

while True:
    connection, address = server_socket.accept()
    new_thread = threading.Thread(target=client, args=(connection, address))
    new_thread.start()
