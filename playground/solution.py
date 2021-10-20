import os
import csv

class CarBase:
	def __init__(self, brand, photo_file_name, carrying):
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = float(carrying)

	def get_photo_file_ext(self):
		return '.' + self.photo_file_name.split('.')[1]


class Car(CarBase):
	car_type = 'car'
	def __init__(self, brand, photo_file_name, carrying, passenger_seats_count=None):
		super(Car, self).__init__(brand, photo_file_name, carrying)
		self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
	car_type = 'truck'
	def __init__(self, brand, photo_file_name, carrying, body_lwh):
		super(Truck, self).__init__(brand, photo_file_name, carrying)
		self.body_length = body_lwh.split('x')[0]
		self.body_width = body_lwh.split('x')[1]
		self.body_height = body_lwh.split('x')[2]

	def get_body_volume(self):
		self.body_params = (self.body_length, self.body_width, self.body_height)
		try:
			self.body_params = list(map(float, self.body_params))
			volume = self.body_params[0] * self.body_params[1] * self.body_params[2]
			return volume
		except ValueError:
			self.body_width, self.body_height, self.body_length = 0, 0, 0
			return self.body_width, self.body_height, self.body_length


class SpecMachine(CarBase):
	car_type = 'spec_machine'
	def __init__(self, brand, photo_file_name, carrying, extra):
		super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
		self.extra = extra


def get_car_list(filename):
	with open(filename, 'r', encoding='utf-8') as file:
		reader = csv.reader(file, delimiter=';')
		col_indexes = enumerate(['car_type', 'brand', 'passenger_seats_count', 'photo_file_name', 'body_whl', 'carrying', 'extra'])
		print(col_indexes)
		#next(reader)
		for row in reader:
			print(row)

get_car_list('coursera_week3_cars.csv')

