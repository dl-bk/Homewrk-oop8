# Метаклас, що може змінювати ім'я класу залежно
# від певних умов або параметрів

class Meta(type):
    def __new__(cls, name, bases, dct):
        try:
            if dct['_modified']:
                new_cls_name = 'Modified' + name
            else: 
                new_cls_name = name
        except KeyError:
            new_cls_name = name
        return super().__new__(cls, new_cls_name, bases, dct) 

class SomeCls(metaclass=Meta):
    _modified = True

    def __init__(self) -> None:
        a = 10
    

obj = SomeCls()

print(obj.__class__.__name__)