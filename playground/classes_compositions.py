from datetime import date
import json

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

	@staticmethod
	def is_age_valid(age):
		return 0 < age < 150


class Planet:

	def __init__(self, name, population = None):
		self.name = name
		self.population = population or []

	def add_human(self, human):
		print(f'Welcome to {self.name} human {human.name}')
		self.population.append(human)


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

class Robot:

	def __init__(self, power):
		self._power = power

	power = property()

	@power.setter
	def power(self, value):
		if value < 0:
			self._power = 0
		else:
			self._power = value

	@power.getter
	def power(self):
		return self._power

	@power.deleter
	def power(self):
		print('Make robot useless')
		del self._power


class Pet:
	def __init__(self, name):
		self.name = name


class Dog(Pet):
	def __init__(self, name, breed = None):
		super().__init__(name)
		self.breed = breed

	def say(self):
		return f'Hello, I am a dog {self.name} of breed {self.breed}'


class ExportJSON:
	def to_json(self):
		pass #return json.dumps({"name": self.name, "breed": self.breed})


class ExDog(Dog, ExportJSON):
	def __init__(self, name, breed=None):
		super().__init__(name, breed)


class WooledDog(Dog, ExportJSON):
	def __init__(self, name, breed=None):
		super(Dog, self).__init__(name)
		self.breed = f'Wooled dog of breed {breed}'

class DogPrivate(Pet):
	def __init__(self, name, breed=None):
		super().__init__(name)
		self.__breed = breed

	def say(self):
		return f'My name is: {self.name}'

	def get_breed(self):
		return self.__breed

class ExDogPrivate(DogPrivate, ExportJSON):
	def get_breed(self):
		return f'Breed is {self.get_breed()}'

class Pet:
	pass

class Cat(Pet):
	pass


print(isinstance(Cat(), Pet))
