#printing half diamond pattern "*"

n=int(input("Enter no of rows to be printed:"))
for i in range(n):
    for j in range(0,i+1):
        print("*",end="")
    print()

for i in range(1,n):
    for j in range(i,n):
        print("*",end="")
    print()

input()
      
