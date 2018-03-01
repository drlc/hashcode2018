from Parser import *
from RidesFactory import *
from CarFactory import *

def main():

    parser = Parser()
    numVehicles, numSteps, listString = parser.readFile("./inputs/a_example.in")

    carFactory = CarFactory(numVehicles, numSteps)
    carList = carFactory.getCarList()

    print carList

    ridesFactory = RidesFactory()
    rideList = ridesFactory.createRides(listString)

    print rideList


    for car in carList:
        nearestRide = carList[0].findNearestRide(rideList)
        print 'Car', nearestRide.indexRide

        for ride in rideList:
            if ride.indexRide == nearestRide.indexRide:
                rideList.remove(ride)

        


if __name__ == '__main__':
    main()