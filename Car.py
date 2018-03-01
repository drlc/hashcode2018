class Car(object):

    def __init__(self, stepsElapsed):
        self.startPointX = 0
        self.startPointY = 0
        self.ridesList = []
        self.stepsElapsed = stepsElapsed

    #def __str__(self):
    #    return 'Car from(' + str(self.startPointX) + ', ' + str(self.startPointY) + ', ' + str(self.ridesList) + ', ' + str(self.stepsElapsed)