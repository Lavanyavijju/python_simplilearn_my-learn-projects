class Employee:
    def readData(self):
        self.__id=int(input("Enter employee id:"))
        self.__name=input("Enter employee name:")
        self.__salary=int(input("Enter employee salary:"))
    def printData(self):
        print("id=",self.__id)
        print("name=",self.__name)
        print("salary=",self.__salary)
    def printCompany():
        print("company=","Microsoft")

emp=Employee()
emp.readData()
emp.printData()
Employee.printCompany()
        
