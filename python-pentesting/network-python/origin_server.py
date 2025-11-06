#!/usr/bin/env python3
import socket
import time

HOST = '127.0.0.1'
PORT = 9090

def handle_client(conn):
    try:
        line = conn.recv(1024).decode().strip()
        if not line:
            return

        if ' ' in line:
            method, path_query = line.split(' ', 1)
        else:
            method, path_query = 'GET', line

        path, _, query = path_query.partition('?')

        if path == '/public':
            conn.sendall(b"Public content (0.9)\n")

        elif path == '/poisonme':
            if 'sleep' in query:
                try:
                    seconds = int(''.join(filter(str.isdigit, query)))
                    conn.sendall(f"Executing payload: sleep {seconds} seconds...\n".encode())
                    time.sleep(seconds)
                    conn.sendall(f"Payload executed: slept {seconds} seconds\n".encode())
                except ValueError:
                    conn.sendall(b"Invalid sleep value\n")
            else:
                conn.sendall(b"SECRET: admin_token=XYZ123\n")
        else:
            conn.sendall(b"404 Not Found\n")

    except Exception as e:
        conn.sendall(f"Error: {e}\n".encode())
    finally:
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(5)
        print(f"Server running on {HOST}:{PORT} (HTTP/0.9 simulation)")

        while True:
            conn, addr = sock.accept()
            handle_client(conn)

if __name__ == "__main__":
    main()
