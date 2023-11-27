# Метаклас, що додає перевірку та обробку аргументів
# __init__ у всіх класах.

class Meta(type):
    def __new__(cls, name, bases, dct):
        if '__init__' in dct:
            original_init = dct['__init__']

            def new_init(self, *args, **kwargs):
                original_init(self, *args, **kwargs)
                if isinstance(args[0], int) and isinstance(args[1], int):
                    self.c = args[0] + args[1]
                    
            dct["__init__"] = new_init
        
        return super().__new__(cls, name, bases, dct)
    
class Cls(metaclass=Meta):
    def __init__(self, a, b, name) -> None:
        self.a = a
        self.b = b
        self.name = name

obj = Cls(10, 12, 'no')

print(obj.c)