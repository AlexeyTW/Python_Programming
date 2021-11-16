import socket
import asyncio

class ClientServerProtocol(asyncio.Protocol):
    srv_data = {}
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        client_request = data.decode()
        print(client_request)
        try:
            if client_request.split()[0] == 'put' and len(client_request.split()) <= 4:
                print('Test!!!')
                key = client_request.split()[1]
                metric = float(client_request.split()[2])
                timestamp = int(client_request.split()[3])
                if key not in self.srv_data.keys():
                    self.srv_data[key] = [(metric, timestamp)]
                else:
                    if timestamp in self.srv_data[key][-1]:
                        self.srv_data[key].pop()
                        self.srv_data[key].append((metric, timestamp))
                    else:
                        self.srv_data[key].append((metric, timestamp))
                self.transport.write(('ok\n\n').encode())
            elif client_request.split()[0] == 'get' and len(client_request.split()) == 2:
                key = client_request.split()[1]
                resp = 'ok\n' + ''.join(self._str_getter(key)) + '\n'
                self.transport.write(resp.encode())
            else:
                self.transport.write('error\nwrong command\n\n'.encode())
        except Exception:
            self.transport.write('error\nwrong command\n\n'.encode())

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

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

run_server('localhost', 8888)