import sys, json, argparse, tempfile, os
from json.decoder import JSONDecodeError

parser = argparse.ArgumentParser()
parser.add_argument('--key', required=True)
parser.add_argument('--value')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path, 'w') as file:
	print(storage_path)
	try:
		json_data = file.read()
		print(json_data)
	except JSONDecodeError:
		json_data = {args.key: []}
		file.write(json_data)
		print('except')

	'''try:
		json_data = file.read()
	except JSONDecodeError:
		json_data = {args.key: []}'''
'''with open ('storage.txt', 'w') as file:
	if args.key and args.value:
		if args.key in json_data:
			json_data[args.key].append(args.value)
		else:
			json_data[args.key] = args.value
		json.dump(json_data, file)
	else:
		print(', '.join(json_data[args.key]))'''




'''parser = argparse.ArgumentParser()
parser.add_argument('--key', required=True)
parser.add_argument('--value', action='append')
args = parser.parse_args()
key = args.key
value = args.value
data = {key: value}
print(data)

if len(args.__dict__) > 1:
	data[key].append(str(value))
	print(data)
	with open('storage.txt', 'w') as file:
		json.dump(data, file)
else:
	print(data[args.key])'''