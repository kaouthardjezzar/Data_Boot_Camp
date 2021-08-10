
#Question 1

class Rectagle:
    def __init__(self, len, larg):
        self.len=len
        self.larg=larg

    def surface (self) :
        return (self.len*self.larg)

rectangle = Rectagle(3,4)
#print(rectangle.surface())

#Question 2

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

#Question 3

class Vehicle:
    pass

#Question 4

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)


