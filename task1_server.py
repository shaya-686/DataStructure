# server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(2)
negative_response = "Fail"
win_response = "Win"
clients = []


def check_word(first_word, second_word):
    return first_word[-1] == second_word[0]


def make_turn(word):
    words.append(word)
    response = f"You should enter the word starts on {word[-1]}"
    clients[1].send(response.encode())
    clients.reverse()


while True:
    print("Waiting...")
    first_client, first_client_address = server.accept()
    clients.append(first_client)
    print(f"Connection from {first_client_address}")

    second_client, second_client_address = server.accept()
    clients.append(second_client)
    print(f"Connection from {second_client_address}")

    clients[0].send("First".encode())
    clients[1].send("Second".encode())

    words = []
    while True:
        client_word = clients[0].recv(1024).decode()
        if client_word == "Finish":
            print("Game over")
            clients[0].send(negative_response.encode())
            clients[1].send(win_response.encode())
            break

        if len(words) == 0:
            make_turn(client_word)
            continue
        else:
            if check_word(words[-1], client_word):
                make_turn(client_word)
                continue
            else:
                clients[0].send(negative_response.encode())
                clients[1].send(win_response.encode())
                break
    print(words)
    clients[0].close()
    clients[1].close()
