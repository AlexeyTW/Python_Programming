from abc import ABC,  abstractmethod


class Hero():

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


class AbstractEffect(Hero, ABC):
    def __init__(self, obj):
        self.base = obj
        self.stats = dict(obj.stats)
        self.positive_effects = list(obj.positive_effects)
        self.negative_effects = list(obj.negative_effects)
        self.common_stats = ['Strength', 'Perception', 'Endurance', 'Charisma',
                             'Intelligence', 'Agility', 'Luck']

    @abstractmethod
    def get_stats(self):
        return self.stats.copy()

    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects.copy()

    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects.copy()


class AbstractPositive(AbstractEffect):
    def __init__(self, obj):
        super().__init__(obj)

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()


class AbstractNegative(AbstractEffect):
    def __init__(self, obj):
        super().__init__(obj)

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()


class Berserk(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj)
        self.positive_effects.append(self.__class__.__name__)

    def get_stats(self):
        self.stats = dict(self.base.stats)

        for key in ['Strength', 'Endurance', 'Agility', 'Luck']:
            self.stats[key] += 7
        for key in ['Perception', 'Charisma', 'Intelligence']:
            self.stats[key] -= 3
        self.stats['HP'] += 50
        return self.stats


class Blessing(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj)
        for key in self.common_stats:
            self.stats[key] += 2

    def get_stats(self):
        return self.stats


class Weakness(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)

        for key in ['Strength', 'Endurance', 'Agility']:
            self.stats[key] -= 4

    def get_stats(self):
        return self.stats


class Curse(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)
        self.negative_effects.append(self.__class__.__name__)

    def get_stats(self):
        self.stats = dict(self.base.stats)
        for key in self.common_stats:
            self.stats[key] -= 2

        return self.stats


class EvilEye(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)
        self.stats['Luck'] -= 10

    def get_stats(self):
        return self.stats



hero = Hero()
print('Hero: ', hero.get_stats(), hero.positive_effects, hero.negative_effects)

bers1 = Berserk(hero)
print('bers1: ', bers1.get_stats(), bers1.get_positive_effects(), bers1.get_negative_effects())
print('Hero: ', hero.get_stats(), hero.positive_effects, hero.negative_effects)

bers2 = Berserk(bers1)
print('bers2: ', bers2.get_stats(), bers2.get_positive_effects(), bers2.get_negative_effects())
print('bers1: ', bers1.stats, bers1.get_positive_effects(), bers1.get_negative_effects())

cur1 = Curse(bers2)
print('Cur1: ', cur1.get_stats(), cur1.get_positive_effects(), cur1.get_negative_effects())

#bers2.base = bers1
#print(bers2.get_stats(), bers2.get_positive_effects())
#print('bers1: ', bers1.get_stats(), bers1.get_positive_effects(), bers1.get_negative_effects())

#blessing = Blessing(hero)
#print(blessing.get_stats(), blessing.get_positive_effects(), blessing.get_negative_effects())