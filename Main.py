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

if __name__ == '__main__':
    main()