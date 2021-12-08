from abc import ABC, abstractmethod

class Engine():
    pass


class ObservableEngine(Engine):
    def __init__(self, achievement):
        self.__subs = set()
        self.achievement = achievement

    def subscribe(self, subscriber):
        self.__subs.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subs.remove(subscriber)

    def notify(self, achievement):
        for subscriber in self.__subs:
            subscriber.update(achievement)


class AbstractObserver(ABC, ObservableEngine):
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


notifier1 = ShortNotificationPrinter({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
#notifier1.update({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})

notifier2 = FullNotificationPrinter({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
#notifier2.update({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})

manager = ObservableEngine({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})

manager.subscribe(notifier1)
manager.subscribe(notifier2)

manager.notify({"title": "Покоритель111", "text": "Дается при выполнении всех заданий в игре"})