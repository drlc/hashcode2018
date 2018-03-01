from Ride import *

class RidesFactory(object):

    def createRides(self, listOfString):
        rideList = []
        for i in range(len(listOfString)):
            ride = Ride(listOfString[i], i)
            rideList.append(ride)
        return rideList
