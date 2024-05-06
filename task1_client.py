# client
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))


def enter_word():
    request = input("Enter the word or press enter to break: ")
    if request:
        client.send(request.encode())
    else:
        print("Finishing game...")
        client.send("Finish".encode())


while True:
    response = client.recv(1024).decode()
    if response in ("Fail", "Win"):
        print(response)
        time.sleep(3)
        break
    if response == "First":
        print("You are the first player")
        enter_word()
    elif response == "Second":
        print("You are the second player")
        print("Waiting for the first player turn...")
    else:
        print(response)
        enter_word()

client.close()
