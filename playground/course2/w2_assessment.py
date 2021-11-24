import pygame
import random
import math

SCREEN_DIM = (500, 500)

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw_point(self, surface, color, center, width):
		pygame.draw.circle(surface, color, center, width)


class Vec2d:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self):
		return self.x[0] - self.y[0], self.x[1] - self.y[1]

	def __sub__(self):
		return self.x[0] + self.y[0], self.x[1] + self.y[1]

	def __mul__(self, v, k):
		self.v = v
		self.k = k
		return self.v[0] * k, self.v[1] * k

	def vec_len(self, x, y):
		self.x = x
		self.y = y
		return math.sqrt(self.x ** 2 + self.y ** 2)

	def int_pair(self, x, y):
		self.x = x
		self.y = y
		return self.__sub__(y, x)


class Polyline:

	def __init__(self, points, speeds):
		self.points = points
		self.speeds = speeds

	def add_point(self, point, speed):
		self.point = point
		self.speed = speed

	def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
		self.points = points
		self.style = style
		self.width = width
		self.color = color

		if style == 'line':
			for p_n in range(-1, len(points) - 1):
				pygame.draw.line(gameDisplay, color,
								 (int(points[p_n][0]), int(points[p_n][1])),
								 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)
		else:
			for p in points:
				pygame.draw.circle(gameDisplay, self.color, (p[0], p[1]), self.width)

	def set_points(self, points, speeds):
		"""функция перерасчета координат опорных точек"""
		self.points = points
		self.speeds = speeds

		for p in range(len(points)):
			print(points[p], speeds[p])
			v = Vec2d(points[p], speeds[p])
			points[p] = v.__add__()
			if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
				speeds[p] = (- speeds[p][0], speeds[p][1])
			if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
				speeds[p] = (speeds[p][0], -speeds[p][1])

'''	def get_point(points, alpha, deg=None):
		if deg is None:
			deg = len(points) - 1
		if deg == 0:
			return points[0]
		return Vec2d.__add__(Vec2d.__mul__(points[deg], alpha), Vec2d.__mul__(get_point(points, alpha, deg - 1), 1 - alpha))

	def get_points(base_points, count):
		alpha = 1 / count
		res = []
		for i in range(count):
			res.append(get_point(base_points, i * alpha))
		return res'''

'''	def get_knot(points, count):
		if len(points) < 3:
			return []
		res = []
		for i in range(-2, len(points) - 2):
			ptn = []
			ptn.append(mul(add(points[i], points[i + 1]), 0.5))
			ptn.append(points[i + 1])
			ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))

			res.extend(get_points(ptn, count))
		return res'''



if __name__ == '__main__':
	pygame.init()
	gameDisplay = pygame.display.set_mode(SCREEN_DIM)
	pygame.display.set_caption('Test game')
	print('Init game')

	working = True
	pause = True
	hue = 0
	color = pygame.Color(0)
	points = []
	speeds = []
	poly = Polyline(points, speeds)

	while working:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				working = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					working = False
				if event.key == pygame.K_r:
					Polyline.points = []
					Polyline.speeds = []
				if event.key == pygame.K_p:
					pause = not pause

			if event.type == pygame.MOUSEBUTTONDOWN:
				point = (event.pos[0], event.pos[1])
				speed = (0.5, 0.5)
				poly.points.append(point)
				poly.speeds.append(speed)



				print(poly.points)
				print(poly.speeds)

		gameDisplay.fill((5, 5, 25))
		hue = (hue + 1) % 360
		color.hsla = (hue, 100, 50, 100)
		poly.draw_points(poly.points)
		poly.draw_points(poly.points, "line", 3, color)
		if not pause:
			poly.set_points(poly.points, poly.speeds)
		#print(type(poly.points))


		#for i in range(len(points)):
		#	pygame.draw.circle(gameDisplay, (255, 255, 155), points[i], 3)
		#	if i > 0:
		#		pygame.draw.circle(gameDisplay, (255, 255, 155), points[i], 3)
		#		pygame.draw.line(gameDisplay, (255, 255, 255, 255), (0, 0), points[i])

		pygame.display.flip()




	pygame.display.quit()
	pygame.quit()
	exit(0)

