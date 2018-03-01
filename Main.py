from Parser import *
from CarFactory import *

def main():

   parser = Parser()
   parser.readFile()
   carFactory = CarFactory(2, 10)
   carList = carFactory.getCarList()

   print carList








if __name__ == '__main__':
   main()