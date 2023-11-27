# Створіть метаклас, який автоматично додає певні
# атрибути до всіх класів, що використовують його.

class AttrMeta(type):
    def __new__(cls, name, bases, dct):
        dct['x'] = True
        dct['f'] = False

        return super().__new__(cls, name, bases, dct)
    
class Cls(metaclass=AttrMeta):
    def __init__(self) -> None:
        a = 11
        b = 12
    
obj = Cls()

print(obj.x)