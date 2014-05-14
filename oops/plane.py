class Airplane:
    __fuel = 0
    maxFuel = 24000
     
    def addFuel(self, volume):
        if(self.__fuel + volume <= 24000):
            self.__fuel = self.__fuel + volume
        else:
            print("Error: You are adding too much fuel!")
            print("Fuelling not possible!")
        self.__printStatus()
 
    def __printStatus(self):
        print("Current fuel:", self.__fuel)