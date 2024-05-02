#server
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(1)

while True:
    print("Waiting...")
    client, address = server.accept()
    print(f"Connection from {address}")

    while True:

        data = client.recv(1024).decode()
        print("Message from client: ", data)

        if data == 'exit':
            break
        response = input("Enter message: ")
        client.send(response.encode())

    client.close()