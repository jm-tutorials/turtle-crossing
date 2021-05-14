from car import Car
import random
from functools import reduce

COLORS = ["red", "orange", "yellow", "teal", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_CARS = 10
LEFT = 180
RIGHT = 0

def ilen(iterable):
    return reduce(lambda sum, element: sum + 1, iterable, 0)

class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE 
        self.minusCars = 0
        self.startingCars()
        self.move()

    def startingCars(self):
        for _ in range(STARTING_CARS):
            self.createCar(start=True)
    
    def createCar(self,start=False):
        color = random.choice(COLORS)
        if start:
            x = random.randint(-300,300)
        else:
            x = random.choice([-300,300])
        position = (x, random.randint(-260, 260))
        if x < -150:
            heading = RIGHT
        else:
            heading = LEFT
        car = Car(color, position, heading)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.move(self.speed)
    
    def increaseSpeed(self):
        self.speed += MOVE_INCREMENT

    def deleteCar(self,car):
        car.hideturtle()
        car.clear()
        del car
        
    def manageOOBCars(self, reset=False):
        for i,car in enumerate(self.cars):
            if reset:
                self.deleteCar(car)
            elif (self.cars[i].xcor() > 310 and  self.cars[i].heading() == 0) or (self.cars[i].xcor() < -310 and self.cars[i].heading() == 180):
                self.deleteCar(car)
                del self.cars[i]
                self.createCar()

    def resetCars(self):
        self.manageOOBCars(True)
        self.cars = []
        self.increaseSpeed()
        self.startingCars()
    
if __name__ == '__main__':
    car_manager = CarManager()