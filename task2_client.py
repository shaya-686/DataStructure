#client
import socket
import json


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
flag = "exit"

while True:

    country = input("Enter country or press enter to break: ")
    if country == "":
        client.send(flag.encode())
        break
    city = input("Enter city or press enter to break: ")
    if city == "":
        client.send(flag.encode())
        break

    request = {"country": country, "city": city}
    client.send(json.dumps(request).encode())

    response = client.recv(1024).decode()
    print(f"Country: {country}, city - {city}, {json.loads(response)}")

client.close()