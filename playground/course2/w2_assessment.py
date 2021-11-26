import pygame
import random
import math

SCREEN_DIM = (800, 600)


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

	def change_speed(self, speeds, coef):
		self.coef = coef
		for s in range(len(speeds)):
			temp = speeds[s]
			speeds[s] = tuple([i * coef for i in temp])
		self.speeds = speeds

	def make_polyline_copy(self):
		pts = list(self.points)
		spds = list(self.speeds)
		new_poly = Polyline(pts, spds)

		for i in range(len(pts)):
			temp = pts[i]
			new_poly.points[i] = tuple([int(i / 2) for i in temp])
		for i in range(len(spds)):
			temp = spds[i]
			new_poly.speeds[i] = tuple([i * 0.7 for i in temp])

		return new_poly


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


class Help:
	def __init__(self):
		pass

	def draw_help(self):
		"""функция отрисовки экрана справки программы"""
		gameDisplay.fill((50, 50, 50))
		font1 = pygame.font.SysFont("courier", 20, bold=True)
		font2 = pygame.font.SysFont("serif", 20)
		data = []
		data.append(["F1", "Show Help"])
		data.append(["R", "Restart"])
		data.append(["P", "Pause/Play"])
		data.append(["Num+", "More points"])
		data.append(["Num-", "Less points"])
		data.append(["Backspace", "Remove base point"])
		data.append(["Key UP", "Increase points speed"])
		data.append(["Key DOWN", "Reduce points speed"])
		data.append(["Slash '/'", "Add one more polyline"])
		data.append(["Backslash '\\'", "Remove one polyline"])
		data.append(["", ""])
		data.append([str(steps), "Current points"])

		pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
			(0, 0), (800, 0), (800, 600), (0, 600)], 5)
		for i, text in enumerate(data):
			gameDisplay.blit(font1.render(
				text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
			gameDisplay.blit(font2.render(
				text[1], True, (128, 128, 255)), (300, 100 + 30 * i))


if __name__ == '__main__':
	pygame.init()
	gameDisplay = pygame.display.set_mode(SCREEN_DIM)
	pygame.display.set_caption('Week2 Peers Assessment')

	working = True
	pause = True
	show_help = False
	hue = 0
	steps = 25
	color = pygame.Color(0)
	points = []
	speeds = []
	poly = Polyline(points, speeds)
	polylines = []
	polylines.append(poly)
	knot = Knot()
	help_ = Help()
	speed_coef = 1

	while working:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				working = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					working = False
				if event.key == pygame.K_r:
					for poly in polylines:
						poly.points = []
						poly.speeds = []
				if event.key == pygame.K_p:
					pause = not pause
				if event.key == pygame.K_KP_PLUS:
					steps += 1
				if event.key == pygame.K_KP_MINUS:
					steps -= 1 if steps > 1 else 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					speed_coef = 1
				if event.key == pygame.K_BACKSPACE:
					for poly in polylines:
						if len(poly.points) > 3:
							poly.points.pop()
				if event.key == pygame.K_UP:
					speed_coef += 0.1
					for poly in polylines:
						poly.change_speed(poly.speeds, speed_coef)
				if event.key == pygame.K_DOWN:
					speed_coef -= 0.1
					for poly in polylines:
						poly.change_speed(poly.speeds, speed_coef)
				if event.key == pygame.K_F1:
					show_help = not show_help
				if event.key == pygame.K_SLASH:
					new_poly = polylines[-1].make_polyline_copy()
					polylines.append(new_poly)
				if event.key == pygame.K_BACKSLASH:
					if len(polylines) > 1:
						polylines.pop()

			if event.type == pygame.MOUSEBUTTONDOWN:
				for poly in polylines:
					point = (event.pos[0] / (polylines.index(poly) + 1), event.pos[1])
					speed = (random.random() * speed_coef, random.random() * speed_coef)
					poly.points.append(point)
					poly.speeds.append(speed)

		gameDisplay.fill((5, 5, 25))
		hue = (hue + 1) % 360
		color.hsla = (hue, 100, 50, 100)
		for poly in polylines:
			poly.draw_points(poly.points)
			poly.draw_points(knot.get_knot(poly.points, steps), 'line', 3, color)

		if not pause:
			for poly in polylines:
				poly.set_points(poly.points, poly.speeds)
		if show_help:
			help_.draw_help()

		pygame.display.flip()

	pygame.display.quit()
	pygame.quit()
	exit(0)
