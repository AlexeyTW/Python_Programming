import socket

with socket.create_connection(('127.0.0.1', 10001)) as sock:
    sock.sendall('hello'.encode('utf-8'))