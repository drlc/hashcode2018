from Parser import *
from RidesFactory import *
from CarFactory import *

def main():

    parser = Parser()

    numVehicles, numSteps, listString = parser.readFile("./inputs/c_no_hurry.in")

    carFactory = CarFactory(numVehicles, numSteps)
    carList = carFactory.getCarList()

    print carList

    ridesFactory = RidesFactory()
    rideList = ridesFactory.createRides(listString)

    print rideList

    finalCarList = []

    while len(carList) > 0:
        print '===='
        for car in carList:

            nearestRide = car.findNearestRide(rideList)

            for ride in rideList:
                if ride.indexRide == nearestRide.indexRide:
                    rideList.remove(ride)

            if car.stepsElapsed == 0:
                carList.remove(car)



    for car in finalCarList:

        file = open("c_testfile.txt", "w")
        for car in carList:
            file.write(str(len(car.ridesList)) + ' ' + car.getRideText() + '\n')


if __name__ == '__main__':
    main()