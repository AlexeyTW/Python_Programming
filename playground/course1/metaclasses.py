from abc import ABCMeta, abstractmethod

def dummy_factory():
	class Class:
		pass
	return Class

Dummy = dummy_factory()
#print(Dummy() is Dummy())

NewClass = type('NewClass', (), {})
#print(NewClass())

class MetaTest(type):
	def __new__(cls, name, parents, attrs):
		#print('Create class {}'.format(name))

		if 'class_id' not in attrs:
			attrs['class_id'] = name.lower()

		return super().__new__(cls, name, parents, attrs)


class A(metaclass=MetaTest):
	pass

#print(A.__dict__)

class Meta(type):
	def __init__(cls, name, bases, attrs):
		print('Initializing class {}'.format(name))

		if not hasattr(cls, 'registry'):
			cls.registry = {}
		else:
			cls.registry[name.lower()] = cls

		super().__init__(name, bases, attrs)


#class Base(metaclass=Meta): pass
#class B(Base): pass
#class C(Base): pass

#print(Base.registry)
#print(Base.__subclasses__())

class Sender(metaclass=ABCMeta):
	@abstractmethod
	def send(self):
		pass

class SenderChild(Sender):
	def send(self):
		pass

#print(SenderChild())

class Python:
	def send(self):
		raise NotImplementedError