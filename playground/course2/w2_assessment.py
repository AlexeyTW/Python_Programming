import pygame
import random
import math


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw_point(self, surface, color, center, width):
		pygame.draw.circle(surface, color, center, width)

if __name__ == '__main__':
	pygame.init()
	gameDisplay = pygame.display.set_mode((500, 500))
	pygame.display.set_caption('Test game')
	print('Init game')

	working = True
	hue = 0
	color = pygame.Color(0)
	points = []

	while working:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				working = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					working = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				point = Point(event.pos[0], event.pos[1])
				points.append((point.x, point.y))

				#print(f'Points: {points}', )

		gameDisplay.fill((5, 5, 25))
		#pygame.draw.circle(gameDisplay, (255, 255, 255), (50, 50), 10)
		#pygame.draw.circle(gameDisplay, (255, 255, 155), (50, 50), 5)
		for i in range(len(points)):
			pygame.draw.circle(gameDisplay, (255, 255, 155), points[i], 3)
			if i > 0:
				pygame.draw.circle(gameDisplay, (255, 255, 155), points[i], 3)
				pygame.draw.line(gameDisplay, (255, 255, 255, 255), (0, 0), points[i])
		#hue = (hue + 1) % 360
		#color.hsla = (hue, 100, 50, 100)

		pygame.display.flip()




	pygame.display.quit()
	pygame.quit()
	exit(0)

