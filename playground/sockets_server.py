import socket
# =================================
'''with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('0.0.0.0', 10001))
    sock.listen(socket.SOMAXCONN)
    while True:
        conn, addr = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode('utf8'))'''

# ======================================
'''sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.123.143', 10001))
sock.listen(socket.SOMAXCONN)

conn, addr = sock.accept()
conn.settimeout(5)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))

conn.close()
sock.close()
'''
# Timeouts ==============================

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        conn.settimeout(10)
        with conn:
            while True:
                try:
                    data = sock.recv(1024)
                except socket.timeout:
                    print('Connection is closed by timeout')
                    break

                if not data:
                    break
                print(data.decode('utf-8'))

'''sock = socket.socket()
sock.bind(('192.168.123.143', 10001))
sock.listen()

conn, addr = sock.accept()
conn.settimeout(30)

while True:
    try:
        data = sock.recv(1024)
    except socket.timeout:
        print('Socket timeout error')
        break

    if not data:
        break

    print(data.decode('utf-8'))
conn.close()
sock.close()'''