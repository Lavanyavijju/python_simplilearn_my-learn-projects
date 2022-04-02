#Read data from file
f1=open("my data.txt","r")

#Read all the lines- All employees
allemployees=f1.readlines()

ch="y"

while(ch=="y"):
    isfound=False
    id=input("Enter employee id:")
    for emp in allemployees:
        data=emp.split(",")
        if(data[0]==id):
            print("Name:",data[1])
            print("Salary:",data[2])
            isfound=True
            break
    if(isfound==False):
        print("Employee not found:")

    ch=input("Do you want to search other employee(y/n):")
