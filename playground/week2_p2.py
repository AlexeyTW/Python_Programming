import json
import functools

def to_json(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		encoder = json.encoder.JSONEncoder()
		json_data = encoder.encode(func(*args, **kwargs))
		return json_data
	return wrapper


@to_json
def get_data(_dict):
	return _dict

result = get_data({"a": 1, "b": 2})

print(result, type(result))
#assert isinstance(result, str)
#assert result == '{"a": 1, "b": 2}'
#assert json.loads(result) == {'a': 1, 'b': 2}
#print('All tests passed!')