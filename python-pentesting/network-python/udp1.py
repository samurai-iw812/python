import socket


host="192.168.0.1"
port=12345

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print(f"Server is listening on {host}:{port}")

while True:
    data, addr = s.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
    s.sendto(b"Hello, client!", addr)