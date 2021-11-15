import socket, os, time

class ClientError(Exception):
	def __init__(self, message):
		self.message = message


class Client:

	def __init__(self, host, port, timeout=None):
		self.host = host
		self.port = port
		self.timeout = timeout
		self.client = socket.create_connection((host, port))

	def put(self, key, value, timestamp=0):
		self.key = key
		self.value = value
		self.timestamp = int(time.time()) if timestamp == 0 else timestamp
		try:
			#float(value)
			#int(timestamp)
			self.client.sendall(('put ' + ' '.join(map(str, [self.key, self.value, self.timestamp])) + '\n').encode('utf-8'))
			# with open('metrics.txt', 'a') as file:
			#	file.write(' '.join(map(str, [key, value, timestamp])) + '\n')
			# print(repr('ok\n\n'))
		except ValueError:
			#print(ClientError)
			raise ClientError

	def get(self, key):
		self.key = key
		srv_dict = {}; i = 0
		try:
			#srv_ans = 'ok' + '\n' + ''.join(self._str_getter(self.key)) + '\n'
			self.client.sendall(('get ' + str(key) + '\n').encode('utf-8'))
			srv_ans = self.client.recv(1024).decode('utf-8')
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
			#print(srv_dict)
			#print(repr(srv_ans))
		except Exception:
			#print(ex)
			raise ClientError

	def _str_getter(self, key: str):
		with open('metrics.txt', 'r') as file:
			rows = file.readlines()
			if key != '*':
				for row in rows:
					if key in row:
						yield row.strip() + '\n'
			else:
				for row in rows:
					yield row.strip() + '\n'

	def close_client(self):
		self.client.close()


	def request_format_check(self, request):
		if request in ['get', 'put', '*']:
			return True
		return False

#client = Client("localhost", 10001)
#client.get('eardruq')
#client.put("eardrum.cpu", 3, 1150864250)