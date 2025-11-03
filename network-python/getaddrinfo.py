from asyncio import protocols
import socket
import types

def get_portnumber(prefix):
    return dict((getattr(socket,a),a) 
    for a in dir(socket) 
        if a.startswith(prefix))

proto_fam = get_portnumber('AF_')
types = get_portnumber('SOCK_')
protocols = get_portnumber('IPPROTO_')

for res in socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP):
    family, socktype, proto, canonname, sockaddr = res
    print(f"Family        : {family}")
    print(f"Socket type   : {socktype}")
    print(f"Protocol      : {proto}")
    print(f"Canonical name: {canonname}")
    print(f"Socket address: {sockaddr}")
    print("-"*50)