class Parser(object):

    def readFile(self, filePath):
        with open(filePath) as f:
            content = f.readlines()

        content = [x.strip() for x in content]

        self.firstlineList = content[0].split(' ')

        numVehicles = int(self.firstlineList[2])
        numSteps = int(self.firstlineList[5])

        listString = content[1:]

        return numVehicles, numSteps, listString
