import tempfile as tempfile
import os.path as path

path_to_file = 'C:\\Users\\ALEXEY~1\\AppData\\Local\\Temp'

class File:
	def __init__(self, filename):
		self.filename = filename
		if not path.exists(filename):
			with open(self.filename, 'w') as f:
				f.write('')

	def __str__(self):
		return self.filename

	def read(self):
		with open(self.filename, 'r') as f:
			return f.read()

	def write(self, data):
		with open(self.filename, 'w') as f:
			f.write(data)

	def __add__(self, other):
		summary_file = File(tempfile.NamedTemporaryFile().name)
		with open(summary_file.__str__(), 'w') as f:
			f.write(self.read() + other.read())
		return summary_file

	def __iter__(self, _start=0):
		self._start = _start
		return self

	def __next__(self):
		with open(self.filename, 'r') as f:
			lst = f.readlines()
		if self._start >= len(lst):
			raise StopIteration
		res = lst[self._start]
		self._start += 1
		return res


file_obj1 = File(path_to_file + '_1')
file_obj1.write('some text\n')
#print(file_obj1.read())
file_obj2 = File(path_to_file + '_2')
file_obj2.write('another text\n')
#print(file_obj2.read())
sum_file = file_obj1 + file_obj2
sum_file1 = sum_file + file_obj2
#print(isinstance(sum_file, File))
print(sum_file.read())
print(sum_file1.read())

#for line in sum_file:
#	print(line)

#for line in sum_file:
#	print(line)