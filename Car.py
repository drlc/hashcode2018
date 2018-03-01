class Car(object):

    def __init__(self, stepsElapsed, index):
        self.startPointX = 0
        self.startPointY = 0
        self.ridesList = []
        self.stepsElapsed = stepsElapsed
        self.index = index

    def findNearestRide(self, rideList):
        nearestRide = None
        for ride in rideList:
            ride.setDistance(abs(self.startPointX - ride.startPositionX) + abs(self.startPointY - ride.startPositionY))
        for ride in rideList:
            if(nearestRide == None or nearestRide.distance > ride.distance):
                nearestRide = ride

        self.ridesList.append(nearestRide)
        self.stepsElapsed = self.stepsElapsed - nearestRide.distance
        self.startPointX = nearestRide.endPositionX
        self.startPointY = nearestRide.endPositionY

        return nearestRide

    def getRideText(self):
        text = ''
        for ride in self.ridesList:
            print self.index, ride.indexRide

            text += str(ride.indexRide) + ' '
        return text


    #def __str__(self):
    #    return 'Car from(' + str(self.startPointX) + ', ' + str(self.startPointY) + ', ' + str(self.ridesList) + ', ' + str(self.stepsElapsed)