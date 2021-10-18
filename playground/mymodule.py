from datetime import date

class Human:

	def __init__(self, name, age=0):
		self._name = name
		self._age = age

	def _say(self, text):
		print(text)

	def say_name(self):
		self._say(f'Hello, I am {self._name}')

	def say_how_old(self):
		self._say(f'I am {self._age} years old')


class Planet:

	def __init__(self, name, population = None):
		self.name = name
		self.population = population or []

	def add_human(self, human):
		print(f'Welcome to {self.name} human {human.name}')
		self.population.append(human)


#solar_system = []
#planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def extract_description(user_string):
	return 'FIFA championship'

def extract_date(user_string):
	return date(2018, 6, 14)

class Event:

	def __init__(self, description, event_date):
		self.description = description
		self.event_date = event_date

	def __str__(self):
		return f'Event "{self.description}" at {self.event_date}'

	@classmethod
	def from_string(cls, user_input):
		description = extract_description(user_input)
		date = extract_date(user_input)
		return cls(description, date)


print(dict.fromkeys("12345"))