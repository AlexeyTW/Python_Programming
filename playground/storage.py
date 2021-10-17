import sys, json, argparse, tempfile, os
from json.decoder import JSONDecodeError, JSONDecoder
from os import path

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
parser = argparse.ArgumentParser()
parser.add_argument('--key', required=True)
parser.add_argument('--value')
args = parser.parse_args()
key, value = args.key, args.value


if key and value:
	with open(storage_path, 'r') as file:
		try:
			storage_data = json.load(file)
		except JSONDecodeError:
			storage_data = {key: []}
		if key in storage_data.keys():
			storage_data[key].append(value)
		else:
			storage_data[key] = [value]
	with open(storage_path, 'w') as target:
		json.dump(storage_data, target)
else:
	if os.path.exists(storage_path):
		with open(storage_path, 'r') as file:
			storage_data = json.load(file)
			if key in storage_data.keys():
				print(', '.join(storage_data[key]))
			else:
				print('None')
	else:
		with open(storage_path, 'w') as file:
			pass