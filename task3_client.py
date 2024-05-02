# client
import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
language_code = {"1": "uk", "2": "en", "3": "pl"}
flag = "exit"

while True:

    language = input("Select target language (1 - uk, 2 - en, 3 - pl) or enter to break: ")
    if language == "":
        client.send(flag.encode())
        break
    if language not in language_code:
        print("Unknown language")
        break
    message = input("Enter message to translate or enter to break:")
    if message == "":
        client.send(flag.encode())
        break
    data = json.dumps({"language": language_code[language], "message": message})
    client.send(data.encode())

    response = client.recv(1024).decode()
    print(response)

client.close()
