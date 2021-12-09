from abc import ABC, abstractmethod

class Engine():
    pass


class ObservableEngine:
# пробую разными способами инициализировать экземпляр
# 1
    def __init__(self):
        self.__subscribers = set()

# 2
    # def __int__(self, achievement):
     #   self.__subscribers = set()
      #  self.achievement = achievement

# 3
    # def __int__(self, achievement):
      #  super().__init__(achievement)
       # self.__subscribers = set()
       # self.achievement = achievement

# при любом варианте инициализации получаю одинаковую ошибку
# также пробую наследовать и не наследовать ObservableEngine от Engine
# ошибка всегда одинаковая

# эти методы оставляю без изменений
    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, achievement):
        for subscriber in self.__subscribers:
            subscriber.update(achievement)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        pass

class ShortNotificationPrinter(AbstractObserver):
    def __init__(self, achievement):
        self.achievements = set()
        self.achievements.add(achievement['title'])

    def update(self, achievement):
        self.achievements.add(achievement['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self, achievement):
        self.achievement = (achievement['title'], achievement['text'])
        self.achievements = []
        if self.achievement not in self.achievements:
            self.achievements.append(self.achievement)

    def update(self, achievement):
        item = (achievement['title'], achievement['text'])
        if item not in self.achievements:
            self.achievements.append(item)

# {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}

not1 = ShortNotificationPrinter({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
not2 = ShortNotificationPrinter({"title": "Покоритель1", "text": "Дается при выполнении всех заданий в игре"})
not3 = FullNotificationPrinter({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})

manager = ObservableEngine()

manager.subscribe(not1)
manager.subscribe(not2)
manager.subscribe(not3)

manager.notify({"title": "111", "text": "111"})
manager.notify({"title": "111", "text": "111"})

manager.unsubscribe(not1)

print(1)