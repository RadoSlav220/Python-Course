class Counter:
    def __init__(self, initial=0, step=1):
        self.__total = initial
        self.__step = step

    @property
    def __total(self):
        return self.__total
    
    @property
    def __step(self):
        return self.__step

    def increment(self):
        self.__total += self.__step
    

class TwowayCounter(Counter): 
    def decrement(self):
        self.__total -= self.__step

counter = TwowayCounter(0, 1)
#print(TwowayCounter.decrement())
