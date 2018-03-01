from RidesFactory import *

def main():
    stringList = ['0 0 1 3 2 9', '1 2 1 0 0 9']
    ridesFactory = RidesFactory()
    rideList = ridesFactory.createRides(stringList)

    print rideList



if __name__ == '__main__':
    main()