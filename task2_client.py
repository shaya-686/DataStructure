# client
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
exit_flag = "exit"
confirm_flag = "ok"
chunk_size = 10
target_file = "file_to_send.txt"


def send_file():
    try:
        with open(target_file, 'rb') as file:
            data = file.read(chunk_size)
            client.send(data)
            while data:
                data = file.read(chunk_size)
                if not data:
                    client.send(exit_flag.encode())
                    break
                client.send(data)
                time.sleep(0.1)
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
    request = input(f"{exit_flag} to break | '{confirm_flag}' to confirm file transferring: ")
    if request == exit_flag:
        print("Finishing program...")
        client.send(exit_flag.encode())
        time.sleep(1)
        break
    elif request == confirm_flag:
        client.send(confirm_flag.encode())
        response = client.recv(1024).decode()
        if response == confirm_flag:
            send_file()
    else:
        print("Unknown operation")
        print("Finishing program...")
        time.sleep(1)
        break
client.close()
