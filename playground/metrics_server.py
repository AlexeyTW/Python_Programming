import socket

server = socket.socket()
server.bind(('localhost', 10001))
server.listen(1)
conn, addr = server.accept()

print('Соединение установлено:', addr)

response = b'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
#response = b'error\nwrong command\n\n'

while True:

    data = conn.recv(1024)
    if not data:
        break
    request = data.decode('utf-8')
    print(f'Получен запрос: {ascii(request)}')
    print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
    conn.send(response)

conn.close()
server.close()