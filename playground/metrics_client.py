import socket, os, time

class ClientError(Exception):
	def __init__(self, message):
		self.message = message


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
		srv_dict = {}; i = 0
		try:
			srv_ans = 'ok' + '\n' + ''.join(self._str_getter(self.key)) + '\n'
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
			print(srv_dict)
		except ClientError as ex:
			print(ex)

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


client = Client("127.0.0.1", 8888)
client.get('fff')