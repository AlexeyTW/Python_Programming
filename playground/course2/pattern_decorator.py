from abc import ABC, abstractmethod


class Creature(ABC):
	@abstractmethod
	def feed(self):
		pass

	@abstractmethod
	def move(self):
		pass

	@abstractmethod
	def make_noise(self):
		pass


class Animal(Creature):
	def feed(self):
		print('I eat grass')

	def move(self):
		print('I can run')

	def make_noise(self):
		print('Gav gav!!!')


class AbstractDecorator(Creature):
	def __init__(self, obj):
		self.obj = obj

	def feed(self):
		self.obj.feed()

	def move(self):
		self.obj.move()

	def make_noise(self):
		self.obj.make_noise()


class Swimming(AbstractDecorator):
	def move(self):
		print('I am swimming creature')

	def make_noise(self):
		print('...')


class Predator(AbstractDecorator):
	def feed(self):
		print('I eat other animals')


class Flying(AbstractDecorator):
	def move(self):
		print('I can fly')

	def make_noise(self):
		print('Quack quack!')


class Fast(AbstractDecorator):
	def move(self):
		print('I am fast!')

animal = Animal()
animal.feed()
animal.move()
animal.make_noise()
print()


duck = Flying(animal)
duck.feed()
duck.move()
duck.make_noise()
print()

fast = Fast(animal)
fast.feed()
fast.move()
fast.make_noise()

fast = Fast(fast)
fast.feed()
fast.move()
fast.make_noise()