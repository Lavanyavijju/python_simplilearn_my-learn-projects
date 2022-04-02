def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

print("4!=",factorial(5))
print("5!=",factorial(8))
print("10!=",factorial(10))

input()
