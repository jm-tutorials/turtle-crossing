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
            x = random.randchoice([-300,300])
        position = (x, random.randint(-260, 260))
        if x < -150:
            heading = RIGHT
        else:
            heading = LEFT
        car = Car(color, position, heading)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.move(STARTING_MOVE_DISTANCE)

    def manageCars(self):
        minusCars = ilen(filter(lambda x: x.xcor() >= 300, self.cars))
        goneCars = [car for car in self.cars if abs(car.xcor()) < 300]
        self.cars = [car for car in self.cars if abs(car.xcor()) < 300]
        for car in goneCars:
            car.reset()
        for _ in STARTING_CARS-minusCars:
            self.createCar()

    def resetCars(self):
        for car in self.cars:
            car.hideturtle()
            car.clear()
            del car
        self.cars = []
        self.startingCars()

if __name__ == '__main__':
    car_manager = CarManager()