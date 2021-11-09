import socket

'''with socket.create_connection(('192.168.123.143', 10001)) as sock:
    sock.sendall('hello'.encode('utf-8'))'''


# ===================================
with socket.create_connection(('192.168.123.143', 10001), 5) as sock:
    sock.settimeout(2)
    try:
        sock.sendall(b'timeout')
    except socket.timeout:
        print('send data timeout')
    except socket.error as ex:
        print('socket error: ', ex)