from abc import ABC, abstractmethod

class Engine:
    pass


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

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
    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        self.achievements.add(achievement['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achievement):
        #item = (achievement['title'], achievement['text'])
        if achievement not in self.achievements:
            self.achievements.append(achievement)


# {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}

not3 = FullNotificationPrinter()

manager = ObservableEngine()

manager.subscribe(not3)

manager.notify({'text': 'Дается за выполнение основного квеста в игре', 'title': 'Покоритель'})
manager.notify({'title': 'Покоритель', 'text': 'Дается за выполнение основного квеста в игре'})


print(1)