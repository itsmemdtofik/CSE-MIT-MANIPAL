class PowerSet:
    "’This class is used to find the power set of a set’"

    def __init__(self):
        self.lis = []
        self.po = []

    def inp(self):
        print('Enter list: ')
        self.lis = [int(x) for x in input().split()]

    def powe(self):
        for i in range(pow(2, len(self.lis))):
            temp = []
            for j in range(len(self.lis)):
                if i & 1 << j:
                    temp.append(self.lis[j])
            self.po.append(temp)

    def pri(self):
        print(self.po)


obj = PowerSet()
print(obj.__doc__)
obj.inp()
obj.powe()
obj.pri()
