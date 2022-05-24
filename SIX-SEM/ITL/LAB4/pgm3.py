class Pow:
    def myInput(self):
        self.x = int(input('Enter base: '))
        self.n = int(input('Enter exponent: '))

    def calc(self):
        self.powerTook = 1
        if self.n >= 0:
            for i in range(self.n):
                self.powerTook *= self.x
        else:
            i = self.n
            while i != 0:
                self.powerTook /= self.x
                i += 1

    def printingThis(self):

        print(self.powerTook)


obj = Pow()
obj.myInput()
obj.calc()
obj.printingThis()
