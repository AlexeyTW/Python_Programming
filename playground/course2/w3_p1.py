from abc import ABC, abstractmethod


class Hero():
	def __init__(self):
		self.positive_effects = []
		self.negative_effects = []
		self.common_stats = ['Strength', 'Perception', 'Endurance', 'Charisma',
							 'Intelligence', 'Agility', 'Luck'
							 ]
		self.stats = {
			"HP": 128,  # health points
			"MP": 42,  # magic points,
			"SP": 100,  # skill points
			"Strength": 15,  # сила
			"Perception": 4,  # восприятие
			"Endurance": 8,  # выносливость
			"Charisma": 2,  # харизма
			"Intelligence": 3,  # интеллект
			"Agility": 8,  # ловкость
			"Luck": 1  # удача
		}

	def get_positive_effects(self):
		return self.positive_effects.copy()

	def get_negative_effects(self):
		return self.negative_effects.copy()

	def get_stats(self):
		return self.stats.copy()

class AbstractEffect(Hero):
	pass


class AbstractPositive(AbstractEffect):
	pass


class AbstractNegative(AbstractEffect):
	pass


class Berserk(AbstractPositive):
	def apply_berserk(self, obj):
		self.obj = obj
		obj.stats['HP'] += 7


class Blessing(AbstractPositive):
	pass


class Weakness(AbstractNegative):
	pass


class Curse(AbstractNegative):
	pass


class EvilEye(AbstractNegative):
	pass


hero = Hero()
bers = Berserk(hero)
print(bers.get_stats())