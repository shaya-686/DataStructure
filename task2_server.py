# server
import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 8080))
server.listen(1)

with open("weather.json", 'r') as file:
    weather_data = json.load(file)

while True:
    print("Waiting...")
    client, address = server.accept()
    print(f"Connection from {address}")

    while True:
        request = client.recv(1024).decode()
        if request == "exit":
            break
        dct = json.loads(request)
        response = "Not found"
        for item in weather_data:
            if item["country"] == dct["country"] and item["city"] == dct["city"]:
                response = {"weather_forecast": item["weather_forecast"]}
                break
        client.send(json.dumps(response).encode())

    client.close()
