# Метаклас, який вносить додаткові перевірки/логіку
# до певних методів у всіх класах.

class AriphMeta(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if callable(value):
                if key == 'divide':
                    def wrapper(a, b):
                        if b == 0: raise ZeroDivisionError("Infinity")
                        result = value(a, b)
                        return result
                    
                    dct[key] = wrapper

        return super().__new__(cls, name, bases, dct)



class Ariphmetic(metaclass=AriphMeta):

    @staticmethod
    def multi(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else: raise ValueError("value must be a number")

    @staticmethod
    def divide(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a / b
        else: raise ValueError("value must be a number")




print(Ariphmetic.divide(10, 0))