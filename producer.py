import socket
import time
import random

server_ip = 'consumer'
server_port = 5000

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            while True:
                number = random.randint(1, 100)
                s.sendall(str(number).encode())
                print(f'Sent: {number}')
                time.sleep(2)
    except ConnectionRefusedError:
        print("Connection refused, retrying in 5 seconds...")
        time.sleep(5)