import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(1)
exit_flag = "exit"
confirm_flag = "ok"
chunk_size = 10
loaded_file = "new_file.txt"


def load_file():
    try:
        with open(loaded_file, 'ab') as file:
            while True:
                client_file_data = client.recv(chunk_size)
                if client_file_data.decode() == exit_flag:
                    break
                file.write(client_file_data)
    except ConnectionError as e:
        print("Message: ", e)
        return False
    except Exception as e:
        print("Message: ", e)
        return False
    else:
        print("File received")
        return True


while True:
    print("Waiting...")
    client, address = server.accept()
    print(f"Connection from {address}")

    while True:
        request = client.recv(1024).decode()
        if request == exit_flag:
            break
        elif request == confirm_flag:
            response = input(f"'{exit_flag}' to break | '{confirm_flag}' to confirm file receiving: ")
            client.send(response.encode())
            if response == confirm_flag:
                load_file()
        else:
            print("Finishing program...")
            time.sleep(1)
            break

    client.close()
