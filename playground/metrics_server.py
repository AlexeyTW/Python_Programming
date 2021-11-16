import socket
import asyncio
from metrics_client import Client, ClientError

class ClientServerProtocol(asyncio.Protocol):
    srv_data = {}
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        client_request = data.decode()
        print('Client request: {}'.format(client_request))
        try:
            if client_request.split()[0] == 'put':
                key = client_request.split()[1]
                metric = float(client_request.split()[2])
                timestamp = int(client_request.split()[3])
                if key not in self.srv_data.keys():
                    self.srv_data[key] = [(metric, timestamp)]
                elif timestamp in self.srv_data[key][-1]:
                    self.srv_data[key].pop()
                    self.srv_data[key].append((metric, timestamp))
                self.transport.write(('ok\n\n').encode())
            elif client_request.split()[0] == 'get' and len(client_request.split()) == 2:
                key = client_request.split()[1]
                resp = 'ok\n' + ''.join(self._str_getter(key)) + '\n'
                print('Server response: ', repr(resp))
                self.transport.write(resp.encode())
            else:
                self.transport.write('error\nwrong command!!!\n\n'.encode())
        except Exception:
            self.transport.write('error\nwrong command!!!\n\n'.encode())
        #print(client_request)
        print(self.srv_data)
        #self.transport.write(('error\nwrong command\n\n').encode())

    def _str_getter(self, key: str):
        if key in self.srv_data.keys():
            for val in self.srv_data[key]:
                get_resp = key + ' ' + ' '.join(map(str, val)) + '\n'
                yield get_resp
        if key == '*':
            for key in self.srv_data.keys():
                for vals in self.srv_data[key]:
                    get_resp = key + ' ' + ' '.join(map(str, vals)) + '\n'
                    yield get_resp

    def _str_gen(self, key: str, iterable):
        yield key + ' ' + ' '.join(map(str, iterable)) + '\n'

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