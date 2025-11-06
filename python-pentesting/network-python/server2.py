import socket

host="192.168.0.1"
port=12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)

conn, addr = s.accept()
print(f"Connection from {addr}")
conn.send(b"Hello, client!")
conn.close()
s.close()