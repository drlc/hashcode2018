class Ride(object):

    def __init__(self, inputString):
        self.startPositionX = int(inputString.split(' ')[0])
        self.startPositionY = int(inputString.split(' ')[1])
        self.endPositionX = int(inputString.split(' ')[2])
        self.endPositionY = int(inputString.split(' ')[3])
        self.earliestStart = int(inputString.split(' ')[4])
        self.latestFinish = int(inputString.split(' ')[5])

    def __str__(self):
        return 'Ride from('+str(self.startPositionX)+','+str(self.startPositionY)+') to('+str(self.endPositionX)+','+str(self.endPositionY)+') earliestStart='+str(self.earliestStart)+' latestFinish='+str(self.latestFinish)