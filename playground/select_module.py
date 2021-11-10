import socket, select

sock = socket.socket()
sock.bind(('', 10001))
sock.listen()

conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()

conn1.setblocking(False)
conn2.setblocking(False)

epoll = select.poll()
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {conn1.fileno(): conn1, conn2.fileno(): conn2}

while True:
	events = epoll.poll(1)
	for fileno, event in events:
		print(fileno, event)
		if event & select.EPOLLIN:
			data = conn_map[fileno].recv(1024)
			print(data.decode('utf-8'))
		elif event & select.EPOLLOUT:
			conn_map[fileno].send(b'sending')