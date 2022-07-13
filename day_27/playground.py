def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
    #return sum(args)



print(add(1,2,3,4))

class Car:
    def __init__(self, **kwarg):
        self.model = kwarg.get("model")
        self.make = kwarg.get("make")
        self.fuel = kwarg.get("fuel")

car = Car(make="Nissan", fuel="disel")
print(car.fuel)
