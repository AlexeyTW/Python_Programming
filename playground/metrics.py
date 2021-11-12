import socket, os, time

class Client:
	def __init__(self, host, port, timeout=None):
		self.host = host
		self.port = port
		self.timeout = timeout

	def put(self, key, value, timestamp=int(time.time())):
		self.key = key
		self.value = value
		self.timestamp = timestamp

		with open('metrics.txt', 'a') as file:
			file.write(' '.join(map(str, [key, value, timestamp])) + '\n')

	def get(self, key):
		self.key = key
		srv_dict = {}
		srv_ans = 'ok' + '\n' + ''.join(self._str_getter(self.key)) + '\n'
		srv_lst = srv_ans[3:].replace('\n', ' ').split()
		while True:
			if i < len(sr)
			srv_dict[srv_lst[i]] = (srv_lst[i + 1], srv_lst[i + 2]) if not i % 3 else None
		print(repr(srv_ans))
		print(srv_lst)
		print(srv_dict)

	def _str_getter(self, key: str):
		with open('metrics.txt', 'r') as file:
			rows = file.readlines()
			if key != '*':
				for row in rows:
					if key in row:
						yield  row.strip() + '\n'
			else:
				for row in rows:
					yield row.strip() + '\n'


client = Client("127.0.0.1", 8888)
client.get('*')