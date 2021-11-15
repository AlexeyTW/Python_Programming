import asyncio


async def hello_world():
	while True:
		print('Hello, world!')
		await asyncio.sleep(1.0)

#loop = asyncio.get_event_loop()
#loop.run_until_complete(hello_world())
#loop.close()

# ===================== SERVER ====================
async def handle_echo(reader, writer):
	data = await reader.read(1024)
	message = data.decode()
	addr = writer.get_extra_info('peername')
	print(f'received {message} from {addr}')
	writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '192.168.123.143', 10001, loop=loop)
server = loop.run_until_complete(coro)

try:
	loop.run_forever()
except KeyboardInterrupt:
	pass



# ===================== CLIENT ====================
'''async def tcp_echo_client(message, loop):
	reader, writer = asyncio.open_connection('192.168.123.143', 10001, loop=loop)
	print(f'Send {message}')
	writer.write(message.encode())
	writer.close()

loop = asyncio.get_event_loop()
message = 'Hello world'
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()'''

# ====================== EXAMPLE =====================

'''async def slow_operation(future):
	await asyncio.sleep(1)
	future.set_result('Future object')

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)
print(future.result())

loop.close()'''

# ====================== EXAMPLE =====================

'''async def sleep_task(num):
	for i in range(5):
		print(f'process task: {num}, iteration: {i}')
		await asyncio.sleep(1)
	return num

loop = asyncio.get_event_loop()
task_list = [loop.create_task(sleep_task(i)) for i in range(2)]
loop.run_until_complete(asyncio.wait(task_list))
loop.close()'''

# ====================== EXAMPLE =====================