import pygame
import os
import Objects
import Service
import Logic

SCREEN_DIM = (800, 600)

pygame.init()
gameDisplay = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("MyRPG")
KEYBOARD_CONTROL = True

if not KEYBOARD_CONTROL:
	import numpy as np
	answer = np.zeros(4, dtype=float)

base_stats = {
    "strength": 20,
    "endurance": 20,
    "intelligence": 5,
    "luck": 5
}

def create_game(sprite_size, is_new):
	global hero, engine, drawer, iteration
	if is_new:
		hero = Objects.Hero(base_stats, Service.create_sprite(
			os.path.join("texture", "Hero.png"), sprite_size))
		engine = Logic.GameEngine()
		Service.service_init(sprite_size)
		Service.reload_game(engine, hero)

size = 60
create_game(size, True)