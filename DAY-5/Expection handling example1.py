try:
    n=int(input("Enter any number:"))
    for i in range(1,11):
        print(n,"x",i,"=",n*i)

except ValueError:
    print("only numbers are allowed,please check it")

input()
                
