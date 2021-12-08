from abc import ABC, abstractmethod

class Engine():
    pass


class ObservableEngine:
    def __init__(self, achievement):
        self.__subscribers = set()
        self.achievement = achievement

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
        super().__init__(achievement)
        self.achievements = set()
        self.achievements.add(achievement['title'])

    def update(self, achievement):
        self.achievements.add(achievement['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self, achievement):
        super().__init__(achievement)
        self.achievement = (achievement['title'], achievement['text'])
        self.achievements = []
        if self.achievement not in self.achievements:
            self.achievements.append(self.achievement)

    def update(self, achievement):
        item = (achievement['title'], achievement['text'])
        if item not in self.achievements:
            self.achievements.append(item)

# {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}

obs = ObservableEngine({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})