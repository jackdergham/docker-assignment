import socket

host = ''
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print('Waiting for connection...')
    
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            with open('/data/received_data.txt', 'a') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f'Received: {data.decode()}')
                    f.write(data.decode() + '\n')
                    f.flush()
            print('Connection closed.')