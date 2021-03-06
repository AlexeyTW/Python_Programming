import socket, os, time

class ClientError(Exception):
	def __init__(self, message):
		self.message = message


class Client:

	def __init__(self, host, port, timeout=None):
		self.host = host
		self.port = port
		self.timeout = timeout
		self.client = socket.create_connection((host, port), 3)

	def response_format_check(self, response: str):
		if response.startswith("ok\n"):
			return True
		else:
			return False

	def put(self, key, value, timestamp=0):
		self.key = key
		self.value = value
		self.timestamp = int(time.time()) if timestamp == 0 else timestamp
		try:
			self.client.sendall(('put ' + ' '.join(map(str, [self.key, self.value, self.timestamp])) + '\n').encode('utf-8'))
			srv_ans = self.client.recv(1024).decode('utf-8')
			print(repr(srv_ans))
			self.response_format_check(srv_ans)
		except ValueError:
			raise ClientError('Incorrect request format')

	def get(self, key):
		self.key = key
		srv_dict = {}; i = 0
		try:
			self.client.sendall(('get ' + str(key) + '\n').encode('utf-8'))
			srv_ans = self.client.recv(1024).decode('utf-8')
			self.response_format_check(srv_ans)
			srv_lst = srv_ans[3:].replace('\n', ' ').split()
			while True:
				if i < len(srv_lst) and not i % 3:
					key = srv_lst[i]
					timestamp = int(srv_lst[i + 2])
					metric = float(srv_lst[i + 1])
					if key in srv_dict.keys():
						srv_dict[key].append((timestamp, metric))
					else:
						srv_dict[key] = [(timestamp, metric)]
					srv_dict[key].sort()
					i += 3
				else:
					break
			return srv_dict
		except Exception:
			raise ClientError('Client error')

	def close_client(self):
		self.client.close()

#client = Client("localhost", 8888)
#client.get('eardrum.cpu')
#client.put("eardrum.cpu", 3, 1150864250)