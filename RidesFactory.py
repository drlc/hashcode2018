from Ride import *

class RidesFactory(object):

    def createRides(self, listOfString):
        rideList = []
        for singleString in listOfString:
            ride = Ride(singleString)
            rideList.append(ride)
        return rideList
