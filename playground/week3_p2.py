import os
import csv

class CarBase:
	def __init__(self, brand, photo_file_name, carrying):
		self.brand = str(brand)
		self.photo_file_name = str(photo_file_name)
		self.carrying = float(carrying)

	def get_photo_file_ext(self):
		if self.photo_file_name.find('.') in [-1, 0, len(self.photo_file_name) - 1]:
			raise ValueError('Incorrect file extension')
		if self.photo_file_name.count('.') != 1:
			raise ValueError('Incorrect file extension')
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
		return self.body_lwh

	@body_lwh.setter
	def body_lwh(self, value):
		try:
			self.body_params = list(map(float, value.split('x')))
			assert len(self.body_params) == 3
			self.body_length = self.body_params[0]
			self.body_width = self.body_params[1]
			self.body_height = self.body_params[2]
		except Exception:
			self.body_width, self.body_height, self.body_length = list(map(float, [0, 0, 0]))


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
			if not (bool(brand) and bool(photo_file_name) and bool(carrying) and bool(car_type)):
				continue
			if car_type == 'car' and bool(passenger_seats_count):
				try:
					obj = Car(brand, photo_file_name, carrying, passenger_seats_count)
					obj.get_photo_file_ext()
					cars.append(obj)
				except ValueError:
					continue
			elif car_type == 'truck':
				try:
					obj = Truck(brand, photo_file_name, carrying, body_lwh)
					obj.get_photo_file_ext()
					cars.append(obj)
				except Exception:
					continue
			elif car_type == 'spec_machine' and bool(extra):
				try:
					obj = SpecMachine(brand, photo_file_name, carrying, extra)
					obj.get_photo_file_ext()
					cars.append(obj)
				except Exception:
					continue
		return cars

cars = get_car_list('coursera_week3_cars.csv')
print(len(cars))
print(cars[-1].__dict__)
print(cars[-1].get_photo_file_ext())
#truck = Truck('nissan', 'nissan.jpg', '1.5', '3x4x5x6')
#print(truck.__dict__)
#print(type(truck.body_length))
#print(truck.get_body_volume())

