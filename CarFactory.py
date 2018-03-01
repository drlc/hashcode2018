from Car import *

class CarFactory(object):

    def __init__(self, numCar, stepsElapsed):
        self.numCar = numCar
        self.stepsElapsed = stepsElapsed
        self.carList = []

    def getCarList(self):
        for i in range(0, self.numCar):
            self.carList.append(Car(self.stepsElapsed, i))
        return self.carList
