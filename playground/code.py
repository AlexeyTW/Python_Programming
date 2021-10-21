class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email

	def get_email_data(self):
		return{'name': self.name, 'email': self.email}

	def __str__(self):
		return f'{self.name} object'

	def __hash__(self):
		return hash(self.email)

	def __eq__(self, other):
		return self.email == other.email


#jane = User('Jane Doe', 'fanedoe@example.com')
#joe = User('Joe Doe', 'fanedoe@example.com')

#print(hash(joe), hash(jane))

class Singleton:
	instance = None
	def __new__(cls):
		if cls.instance is None:
			cls.instance = super().__new__(cls)
		return cls.instance

#a = Singleton()
#b = Singleton()
#print(id(a) == id(b))

class Researcher:
	def __getattr__(self, item):
		return f'Attribute {item} is not found'

	def __getattribute__(self, item):
		print(f'Trying to access attribute "{item}"')
		return object.__getattribute__(self, item)

#obj = Researcher()
#print(obj.attr)

class Ignorant:
	def __setattr__(self, key, value):
		print('Do not set method {}!'.format(key))

#obj = Ignorant
#obj.math = 123
#print(obj.__dict__)

#class Setter:
	#def __getitem__(self, item):