from abc import ABC,  abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
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
        self.positive_effects = self.base.positive_effects.copy()
        self.negative_effects = self.base.negative_effects.copy()

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
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append(self.__class__.__name__)

        self.negative_effects = self.base.get_negative_effects()

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.base.negative_effects.copy()


class AbstractNegative(AbstractEffect):
    def __init__(self, obj):
        super().__init__(obj)
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append(self.__class__.__name__)

        self.positive_effects = self.base.get_positive_effects()

    def get_positive_effects(self):
        return self.base.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()


class Berserk(AbstractPositive):
    def get_stats(self):
        if self.base.get_stats():
            self.stats = self.base.get_stats()
            for key in ['Strength', 'Endurance', 'Agility', 'Luck']:
                self.stats[key] += 7
            for key in ['Perception', 'Charisma', 'Intelligence']:
                self.stats[key] -= 3
            self.stats['HP'] += 50
        return self.stats


class Blessing(AbstractPositive):
    def get_stats(self):
        self.stats = self.base.get_stats()
        if self.base.get_stats():
            for key in self.common_stats:
                self.stats[key] += 2
        return self.stats


class Weakness(AbstractNegative):
    def get_stats(self):
        if self.base.get_stats():
            self.stats = self.base.get_stats()
            for key in ['Strength', 'Endurance', 'Agility']:
                self.stats[key] -= 4
        return self.stats


class Curse(AbstractNegative):
    def get_stats(self):
        if self.base.get_stats():
            self.stats = self.base.get_stats()
            for key in self.common_stats:
                self.stats[key] -= 2
        return self.stats

class EvilEye(AbstractNegative):
    def get_stats(self):
        if self.base.get_stats():
            self.stats = self.base.get_stats()
            self.stats['Luck'] -= 10
        return self.stats


hero = Hero()
print('Hero: ', hero.get_stats(), hero.get_positive_effects(), hero.get_negative_effects())

bers1 = Berserk(hero)
print('Bers1: ', bers1.get_stats(), bers1.get_positive_effects(), bers1.get_negative_effects())

#cur1 = Curse(bers1)
#print('Curse1: ', cur1.get_stats(), cur1.get_positive_effects(), cur1.get_negative_effects())

bers2 = Berserk(bers1)
print('Bers2: ', bers2.get_stats(), bers2.get_positive_effects(), bers2.get_negative_effects())

bers3 = Berserk(bers2)
print('Bers3: ', bers3.get_stats(), bers3.get_positive_effects(), bers3.get_negative_effects())

bers3.base = bers1
print('Bers3 updated: ', bers3.get_positive_effects(), bers3.get_negative_effects())

#bers2.base = bers1
#print('Bers2: ', bers2.get_stats(), bers2.get_positive_effects(), bers2.get_negative_effects())
#cur1 = Curse(bers2)
#print(cur1.get_stats(), cur1.get_positive_effects(), cur1.get_negative_effects())

#cur1.base = bers1
#print(cur1.get_stats(), cur1.get_positive_effects(), cur1.get_negative_effects())

#bless = Blessing(cur1)
#print('Bless: ', bless.get_stats())

