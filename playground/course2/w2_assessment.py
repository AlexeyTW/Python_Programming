import pygame
import random
import math

SCREEN_DIM = (500, 500)


class Vec2d:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self):
		return self.x[0] + self.y[0], self.x[1] + self.y[1]

	def __sub__(self):
		return self.x[0] - self.y[0], self.x[1] - self.y[1]

	def __mul__(self, v, k):
		self.v = v
		self.k = k
		return self.v[0] * k, self.v[1] * k

	def vec_len(self, x, y):
		return math.sqrt(self.x ** 2 + self.y ** 2)

	def int_pair(self, x, y):
		self.x = x
		self.y = y
		return self.__sub__(self.y, self.x)


class Polyline:

	def __init__(self, points, speeds):
		self.points = points
		self.speeds = speeds

	def add_point(self, point, speed):
		self.point = point
		self.speed = speed

	def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
		#self.points = points
		#self.style = style
		#self.width = width
		#self.color = color

		if style == 'line':
			for p_n in range(-1, len(points) - 1):
				pygame.draw.line(gameDisplay, color,
								 (int(points[p_n][0]), int(points[p_n][1])),
								 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)
		else:
			for p in points:
				pygame.draw.circle(gameDisplay, color, (p[0], p[1]), width)

	def set_points(self, points, speeds):
		"""функция перерасчета координат опорных точек"""
		for p in range(len(points)):
			v = Vec2d(points[p], speeds[p])
			points[p] = v.__add__()
			if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
				speeds[p] = (- speeds[p][0], speeds[p][1])
			if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
				speeds[p] = (speeds[p][0], -speeds[p][1])


class Knot(Polyline):
	def __init__(self):
		super().__init__(points, speeds)

	def get_point(self, points, alpha, deg=None):
		if deg is None:
			deg = len(points) - 1
		if deg == 0:
			return points[0]
		x = (points[deg][0] * alpha, points[deg][1] * alpha)
		y = (self.get_point(points, alpha, deg - 1)[0] * (1 - alpha),
			self.get_point(points, alpha, deg - 1)[1] * (1 - alpha))
		return x[0] + y[0], x[1] + y[1]

	def get_points(self, base_points, count):
		alpha = 1 / count
		res = []
		for i in range(count):
			res.append(self.get_point(base_points, i * alpha))
		return res

	def get_knot(self, points, count):
		if len(points) < 3:
			return []
		res = []
		for i in range(-2, len(points) - 2):
			ptn = []
			v = Vec2d(points[i], points[i + 1])
			ptn.append(v.__mul__(v.__add__(), 0.5))
			ptn.append(points[i + 1])
			v = Vec2d(points[i + 1], points[i + 2])
			ptn.append(v.__mul__(v.__add__(), 0.5))
			res.extend(self.get_points(ptn, count))
		return res


if __name__ == '__main__':
	pygame.init()
	gameDisplay = pygame.display.set_mode(SCREEN_DIM)
	pygame.display.set_caption('Week2 Peers Assessment')

	working = True
	pause = True
	hue = 0
	steps = 35
	color = pygame.Color(0)
	points = []
	speeds = []
	poly = Polyline(points, speeds)
	knot = Knot()

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
				speed = (random.random(), random.random())
				poly.points.append(point)
				poly.speeds.append(speed)

		gameDisplay.fill((5, 5, 25))
		hue = (hue + 1) % 360
		color.hsla = (hue, 100, 50, 100)
		poly.draw_points(poly.points)
		poly.draw_points(knot.get_knot(poly.points, steps), 'line', 3, color)

		if not pause:
			poly.set_points(poly.points, poly.speeds)

		pygame.display.flip()

	pygame.display.quit()
	pygame.quit()
	exit(0)

