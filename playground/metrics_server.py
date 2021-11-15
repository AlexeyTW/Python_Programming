import socket
import asyncio

class ClientServerProtocol(asyncio.Protocol):


    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        srv_data = {}
        client_request = data.decode()
        '''if client_request.split()[0] == 'put':
            key = client_request.split()[1]
            metric = float(client_request.split()[2])
            timestamp = int(client_request.split()[3])
            if key not in srv_data.keys():
                srv_data[key] = [(timestamp, metric)]
            srv_data[key].append((timestamp, metric))'''

        print(client_request)
        print(srv_data)
        #self.transport.write(('ok\n' + client_request + '\n\n').encode())

loop = asyncio.get_event_loop()
coro = loop.create_server(ClientServerProtocol, 'localhost', 8888)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.close()

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()













'''server = socket.socket()
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
server.close()'''