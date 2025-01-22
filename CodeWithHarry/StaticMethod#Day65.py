class Math:
    def __init__(self,num):
        self.num=num

    #This is instance method
    def addtonum(self,n):
        self.num=self.num + n

    @staticmethod
    def add(a,b):
        return a+b

if __name__=="__main__":
    a=Math(5)
    print(a.num)
    a.addtonum(6)
    print(a.num)
    print(a.add(4,5))
