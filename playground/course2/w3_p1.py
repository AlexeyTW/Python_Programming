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
        self.positive_effects = obj.positive_effects
        self.negative_effects = obj.negative_effects

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass


class AbstractPositive(AbstractEffect):
    def __init__(self, obj):
        super().__init__(obj)
        self.base = obj
        self.positive_effects.append(self.__class__.__name__)

    def get_positive_effects(self):
        self.base.get_positive_effects()

    def get_negative_effects(self):
        self.base.get_negative_effects()


class AbstractNegative(AbstractEffect):
    def __init__(self, obj):
        super().__init__(obj)
        self.base = obj
        self.negative_effects.append(self.__class__.__name__)

    def get_positive_effects(self):
        return self.positive_effects

    def get_negative_effects(self):
        return self.negative_effects


class Berserk(AbstractPositive):
    def get_stats(self):
        for key in ['Strength', 'Endurance', 'Agility', 'Luck']:
            self.stats[key] += 7
        for key in ['Perception', 'Charisma', 'Intelligence']:
            self.stats[key] -= 3
        self.stats['HP'] += 50
        return self.stats

    def get_positive_effects(self):
        return self.positive_effects

    def get_negative_effects(self):
        return self.negative_effects

class Curse(AbstractNegative):
    def get_stats(self):
        for key in self.common_stats:
            self.stats[key] -= 2
        return self.stats

hero = Hero()
print('Hero: ', hero.get_stats(), hero.get_positive_effects(), hero.get_negative_effects())

bers1 = Berserk(hero)
print('Bers1: ', bers1.get_stats(), bers1.get_positive_effects(), bers1.get_negative_effects())

brs2 = Berserk(bers1)
print('Brs 2: ', brs2.stats, brs2.get_positive_effects(), brs2.get_negative_effects())

cur1 = Curse(brs2)
print(cur1.get_stats())

