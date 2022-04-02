n=int(input("Enter any number:"))
isprime=True
for i in range(2,n):
    if(n%i==0):
        isprime=False
        break
if(isprime==True):
    print("prime number")
else:
    print("Not a prime number")

input()
