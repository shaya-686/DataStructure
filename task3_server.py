#server
import socket
import json
from googletrans import Translator

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 8080))
server.listen(1)

while True:
    print("Waiting...")
    client, address = server.accept()
    print(f"Connection from {address}")

    while True:

        request = client.recv(1024).decode()
        if request == "exit":
            break
        dct = json.loads(request)

        translator = Translator()
        response = translator.translate(dct["message"], dest=dct["language"]).text
        client.send(response.encode())

    client.close()