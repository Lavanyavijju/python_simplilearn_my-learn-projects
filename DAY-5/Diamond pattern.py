n=int(input("Enter any number:"))

#Top half
for r in range(1,n):
    #for spaces
    for s in range(n,r,-1):
        print(" ",end="")
    #for stars
    for st in range(1,2*r):
        print("*",end="")
    print("")

#bottom half
for r in range(n,0,-1):
    #for spaces
    for s in range(n,r,-1):
        print(" ",end="")
    #for stars
    for st in range(1,2*r):
        print("*",end="")
    print("")


input()


        
