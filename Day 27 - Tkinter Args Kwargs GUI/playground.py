def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

# print(add(1,23,2,11,1,5,5,5,2))

def calculate(n, **kwargs):
    print(n)
    print(kwargs["add"])
    print(kwargs["mul"])

calculate(2, add=5, mul=7)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(model="GTR")
print(my_car.make)