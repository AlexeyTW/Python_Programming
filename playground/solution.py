import os
import csv

class CarBase:
	def __init__(self, brand, photo_file_name, carrying):
		self.brand = str(brand)
		self.photo_file_name = str(photo_file_name)
		self.carrying = float(carrying)

	def get_photo_file_ext(self):
		return '.' + self.photo_file_name.split('.')[1]


class Car(CarBase):
	car_type = 'car'
	def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
		super(Car, self).__init__(brand, photo_file_name, carrying)
		self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
	car_type = 'truck'
	def __init__(self, brand, photo_file_name, carrying, body_lwh):
		super(Truck, self).__init__(brand, photo_file_name, carrying)
		self.body_lwh = body_lwh

	@property
	def body_lwh(self):
		return self._body_lwh

	@body_lwh.setter
	def body_lwh(self, value):
		try:
			self.body_params = list(map(float, value.split('x')))
			self.body_length = self.body_params[0]
			self.body_width = self.body_params[1]
			self.body_height = self.body_params[2]
		except ValueError:
			self.body_width, self.body_height, self.body_length = 0, 0, 0


	def get_body_volume(self):
		return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
	car_type = 'spec_machine'
	def __init__(self, brand, photo_file_name, carrying, extra):
		super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
		self.extra = str(extra)


def get_car_list(filename):
	cars = []
	with open(filename, 'r', encoding='utf-8') as file:
		reader = csv.reader(file, delimiter=';')
		next(reader)
		for row in reader:
			if len(row) < 7:
				continue
			car_type, brand, passenger_seats_count, photo_file_name, body_lwh, carrying, extra = row
			if car_type == 'car':
				try:
					obj = Car(brand, photo_file_name, carrying, passenger_seats_count)
					cars.append(obj)
				except ValueError:
					continue
			elif car_type == 'truck':
				try:
					obj = Truck(brand, photo_file_name, carrying, body_lwh)
					cars.append(obj)
				except Exception as ex:
					print(ex.args[0])
		return cars

#cars = get_car_list('coursera_week3_cars.csv')
#print(cars[1].__dict__)
truck = Truck('Nissan', 'nissan.jpeg', '1.5', '2x8x1.87')
print(truck.__dict__)
print(truck.get_body_volume())

