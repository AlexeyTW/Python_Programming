class Descriptor:
    def __get__(self, obj, obj_type):
        print('get')

    def __set__(self, obj, value):
        print('set')

    def __delete__(self, obj):
        print('delete')


class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)


class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('log.txt', 'a') as file:
            file.write(str(value))
        self.amount = value

    def method(self):
        pass


class Account:
    amount = ImportantValue(100)


#account_inst = Account()
#account_inst.amount = 150

class Class:
    val = Value()

inst = Class()
inst.val = 10

print(inst.val)