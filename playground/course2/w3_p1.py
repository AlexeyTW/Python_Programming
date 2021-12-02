from abc import ABC,  abstractmethod


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
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(ABC, Hero):
    def __init__(self, obj):
        self.base = obj
        self.common_stats = ['Strength', 'Perception', 'Endurance', 'Charisma',
                             'Intelligence', 'Agility', 'Luck']

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass


'''class AbstractPositive(AbstractEffect, ABC):
    def __init__(self, obj):
        self.positive_effects.append(obj.__class__.__name__)



class AbstractNegative(AbstractEffect):
    def get_stats(self):
        self.get_stats()

    def get_positive_effects(self):
        self.get_positive_effects()

    def get_negative_effects(self):
        self.get_negative_effects()'''


class Berserk(AbstractEffect):
    def get_stats(self):
        self.stats = dict(self.base.stats)
        for key in ['Strength', 'Endurance', 'Agility', 'Luck']:
            self.stats[key] += 7
        for key in ['Perception', 'Charisma', 'Intelligence']:
            self.stats[key] -= 3
        self.stats['HP'] += 50
        return self.stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append(self.__class__.__name__)
        return self.positive_effects

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append(self.__class__.__name__)
        return self.negative_effects


hero = Hero()
print('Hero: ', hero.get_stats(), hero.get_positive_effects(), hero.get_negative_effects())

bers1 = Berserk(hero)
print('Bers1: ', bers1.get_stats(), bers1.get_positive_effects(), bers1.get_negative_effects())

