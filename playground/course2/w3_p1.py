from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.common_stats = ['Strength', 'Perception', 'Endurance', 'Charisma',
                             'Intelligence', 'Agility', 'Luck']
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
        # return self.positive_effects.copy()
        print(self.positive_effects.copy())

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        # return self.stats.copy()
        print(self.stats.copy())


class AbstractEffect(Hero):
    pass


class AbstractPositive(AbstractEffect):
    pass


class AbstractNegative(AbstractEffect):
    pass


class Berserk(AbstractPositive):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj

        for key in ['Strength', 'Endurance', 'Agility', 'Luck']:
            self.obj.stats[key] += 7
        for key in ['Perception', 'Charisma', 'Intelligence']:
            self.obj.stats[key] -= 3
        self.obj.stats['HP'] += 50
        obj.positive_effects.append(self.__class__.__name__)


class Blessing(AbstractPositive):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj

        for key in self.common_stats:
            self.stats[key] += 2


class Weakness(AbstractNegative):
    pass


class Curse(AbstractNegative):
    pass


class EvilEye(AbstractNegative):
    pass


hero = Hero()
print(hero.stats)

brs1 = Berserk(hero)
brs1.get_stats()
#hero.get_stats()

brs2 = Berserk(brs1)
brs2.get_stats()
#hero.get_stats()
