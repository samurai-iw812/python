import socket

host="192.168.0.1" #server address
port=12345 #server port

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object (IPv4, TCP)
client.connect((host, port)) #connect to the server

print(client.recv(1024).decode()) #receive a message from the server
client.close() #close the connection