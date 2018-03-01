from Parser import *
from RidesFactory import *
from CarFactory import *

def main():

    parser = Parser()
    numVehicles, numSteps, listString = parser.readFile("./inputs/e_high_bonus.in")

    carFactory = CarFactory(numVehicles, numSteps)
    carList = carFactory.getCarList()

    print carList

    ridesFactory = RidesFactory()
    rideList = ridesFactory.createRides(listString)

    print rideList


    for car in carList:
        nearestRide = car.findNearestRide(rideList)
        print 'Car', nearestRide.indexRide

        for ride in rideList:
            if ride.indexRide == nearestRide.indexRide:
                rideList.remove(ride)

    file = open("e_testfile.txt", "w")
    for car in carList:
        file.write(str(len(car.ridesList)) + ' ' + car.getRideText() + '\n')


if __name__ == '__main__':
    main()