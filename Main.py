from RidesFactory import *
from CarFactory import *

def main():
    stringList = ['0 0 1 3 2 9', '1 2 1 0 0 9']
    ridesFactory = RidesFactory()
    rideList = ridesFactory.createRides(stringList)
    carFactory = CarFactory(2, 10)
    carList = carFactory.getCarList()

    print carList
    print rideList


if __name__ == '__main__':
    main()