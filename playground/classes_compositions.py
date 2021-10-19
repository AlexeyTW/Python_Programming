class Pet:
	def __init__(self):
		pass

	def pet_method(self):
		pass

class Dog(Pet):
	def method(self):
		super(Dog, self).pet_method()

print(isinstance(Dog(), Dog))