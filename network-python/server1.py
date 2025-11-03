import socket

host="192.168.0.1" #server address
port=12345 #server port

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object (IPv4, TCP)
server.bind((host, port)) #bind the socket to the host and port
server.listen(5) #listen for connections (max 5 connections)

print(f"Server is listening on {host}:{port}")
while True:
    client_socket, client_address = server.accept() #accept a connection from a client
    print(f"Connection from {client_address}")
    client_socket.send(b"Hello, client!") #send a message to the client
    client_socket.close() #close the connection
server.close() #close the server