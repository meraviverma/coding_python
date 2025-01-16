class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def changeCompany(cls,newCompany): #here you can write self,cls, monkey enything decorator is important
        cls.company=newCompany


if __name__=="__main__":
    obj=Employee()
    obj.name="Ravi"
    #print(obj.show()) #Here it will print None as well as show method doesn't return anything. To avoid this don't
    # put under print
    obj.show()
    obj.changeCompany("Tesla")
    obj.show()

    print(obj.company)
    print(Employee.company)

    obj2=Employee()
    print(obj2.company)

"""
Output:
The name is Ravi and company is Apple
The name is Ravi and company is Tesla
Tesla
Tesla
Tesla

"""