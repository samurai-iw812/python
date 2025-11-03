import socket

host="192.168.0.1"
port=12345

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
    s.send(b"Hello, server!")
    data = s.recv(1024)
    print(f"Received from server: {data.decode()}")
    s.close()
except socket.error as err:
    print(f"Socket error: {err}")
    s.close()

