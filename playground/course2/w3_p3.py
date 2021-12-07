from abc import ABC, abstractmethod

class ObservableEngine:
    def __init__(self):
        self.__subs = set()

    def subscribe(self, subscriber):
        self.__subs.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subs.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subs:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        pass

class ShortNotificationPrinter(AbstractObserver):
    def __init__(self, achievement):
        self.achievements = set()
        self.achievements.add(achievement)

    def update(self, achievement):
        self.achievements.add(achievement)
        print(self.achievements)

class FullNotificationPrinter(AbstractObserver):
    def __init__(self, achievement):
        self.achievement = achievement
        self.achievements = []
        if self.achievement not in self.achievements:
            self.achievements.append(self.achievement)

    def update(self, achievement):
        if achievement not in self.achievements:
            self.achievements.append(achievement)

        print(self.achievements)

notifier1 = ShortNotificationPrinter('Hero')
notifier1.update('King')
#notifier2 = ShortNotificationPrinter('King')
notifier3 = FullNotificationPrinter('Test1')
notifier3.update('TTT')
notifier3.update('TTT1')
#notifier4 = FullNotificationPrinter('Test2')

'''manager = ObservableEngine()

manager.subscribe(notifier1)
manager.subscribe(notifier2)
manager.subscribe(notifier3)
manager.subscribe(notifier4)

manager.notify('King')
'''
