import sys, json, argparse, tempfile
from json.decoder import JSONDecodeError

with open('storage.txt', 'r') as file:
	try:
		json_data = json.load(file)
	except JSONDecodeError:
		json_data = {}
	with open ('storage.txt', 'w') as file:
		parser = argparse.ArgumentParser()
		parser.add_argument('--key', required=True)
		parser.add_argument('--value')
		args = parser.parse_args()
		if args.key and args.value:
			if args.key in json_data:
				json_data[args.key].append(args.value)
			else:
				json_data[args.key] = args.value
			json.dump(json_data, file)


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


