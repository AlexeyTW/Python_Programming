class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""

E_INT, E_STR, E_FLOAT = 'INT', 'STR', 'FLOAT'

class EventGet:
    def __init__(self, type_):
        self.kind = {int: E_INT, str: E_STR, float: E_FLOAT}[type_]
        self.prop = None


class EventSet:
    def __init__(self, value):
        self.kind = {int: E_INT, str: E_STR, float: E_FLOAT}[type(value)]
        self.prop = value


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_INT:
            if event.prop is None:
                return obj.integer_field
            else:
                obj.integer_field = event.prop
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_FLOAT:
            if event.prop is None:
                return obj.float_field
            else:
                obj.float_field = event.prop
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_STR:
            if event.prop is None:
                return obj.string_field
            else:
                obj.string_field = event.prop
        else:
            return super().handle(obj, event)




obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"
chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
chain.handle(obj, EventGet(int))
chain.handle(obj, EventGet(float))
chain.handle(obj, EventGet(str))
chain.handle(obj, EventSet(0.5))