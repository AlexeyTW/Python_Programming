from abc import ABC, abstractmethod


class Delivery:
    """
    Класс описывающий объект, содержащий информацию о доставке для заказа
    """

    # для упрощения кода, пусть будет только один атрибут
    # time_delivery - время доставки, не будем добавлять id
    # заказа и другие "нужные" данные
    def __init__(self, time_delivery=None):
        self.time_delivery = time_delivery or 10

    def get_time_delivery(self):
        """возвращает время доставки по заказу"""
        return self.time_delivery


# На время доставки могут влиять разные факторы - проведение
# специальных акций, выбор специальных условий при заказе,
# например: экспресс доставка или оплата наличными. В начальный
# момент времени (при написании кода) нельзя учесть все возможные
#  действия, которые возможно будут добавлены.
class AbstractDeliveryAction(ABC, Delivery):
    """Абстрактный для всех действий класс"""

    def __init__(self, base):
        self.base = base
        self.actions = []

    @abstractmethod
    def get_time_delivery(self):
        pass


class SpecialOffer(AbstractDeliveryAction):
    """Специальное предложение - сокращает срок доставки на 3 дня"""

    def get_time_delivery(self):
        return self.base.get_time_delivery() - 3


class ExpressDelivery(AbstractDeliveryAction):
    """Экспресс доставка сокращает срок доставки на 10 дней"""

    def get_time_delivery(self):
        return self.base.get_time_delivery() - 5


class CardPayment(AbstractDeliveryAction):
    """Оплата картой увеличивает срок доставки на 1 день"""

    def get_time_delivery(self):
        return self.base.get_time_delivery() + 1


# обратите внимание, что мы не изменяем непосредственно self.base
# а возвращаем его изменененную копию, так происходит магия декораторов
# создадим заказ
order = Delivery()
print(order.get_time_delivery())
# будем применять действия к заказу, в зависимости от желания
# заказчика и действующих акций
order_expr = ExpressDelivery(order)
print(order_expr.get_time_delivery())
order_expr_spec = SpecialOffer(order_expr)
print(order_expr_spec.get_time_delivery())
order_total = CardPayment(order_expr_spec)
print(order_total.get_time_delivery())

# уберем экспресс доставку, если вдруг заказчик передумал
order_expr_spec.base = order_expr_spec.base.base
print(order_total.get_time_delivery())
# вывод справа в окне терминала -->
# такая реализация позволяет без проблем добавлять новые действия
# и их можно без проблем применять к уже существующим заказам
