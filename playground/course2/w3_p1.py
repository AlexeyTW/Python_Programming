from abc import ABC, abstractmethod


class Hero(ABC):
    positive_effects = []
    negative_effects = []
    stats = {
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
    common_stats = ['Strength', 'Perception', 'Endurance', 'Charisma',
                    'Intelligence', 'Agility', 'Luck']
    '''def __init__(self):
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
        }'''


    def get_positive_effects(self):
        # return self.positive_effects.copy()
        print(self.positive_effects.copy())


    def get_negative_effects(self):
        return self.negative_effects.copy()


    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero):
    def __init__(self, obj):
        self.obj = obj

    def get_stats(self):
        return self.obj.stats.copy()


class AbstractPositive(AbstractEffect):
    '''def __init__(self, obj):
        super().__init__(obj)
        self.obj = obj
        self.obj.positive_effects.append(self.__class__.__name__)'''

    def get_positive_effects(self):
        return self.obj.positive_effects.copy()


class AbstractNegative(AbstractEffect):
    '''def __init__(self, obj):
        super().__init__(obj)
        self.obj = obj
        self.obj.negative_effects.append(self.__class__.__name__)'''

    def get_negative_effects(self):
        return self.negative_effects.copy()


class Berserk(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj)

        for key in ['Strength', 'Endurance', 'Agility', 'Luck']:
            self.obj.stats[key] += 7
        for key in ['Perception', 'Charisma', 'Intelligence']:
            self.obj.stats[key] -= 3
        self.obj.stats['HP'] += 50


class Blessing(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj)

        for key in self.obj.common_stats:
            self.stats[key] += 2


class Weakness(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)

        for key in ['Strength', 'Endurance', 'Agility']:
            self.obj.stats[key] -= 4


class Curse(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)

        for key in self.obj.common_stats:
            self.obj.stats[key] -= 2


class EvilEye(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)

        self.obj.stats['Luck'] -= 10



hero = Hero()
print(hero.get_stats())
print(hero.positive_effects, hero.negative_effects)

bers1 = Berserk(hero)
print(bers1.get_stats())
print(bers1.positive_effects, bers1.negative_effects)

curse1 = Curse(bers1)
print(curse1.get_stats())
print(curse1.positive_effects, curse1.negative_effects)

ee = EvilEye(bers1)
print(ee.stats)
print(ee.positive_effects, ee.negative_effects)