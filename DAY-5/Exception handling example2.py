try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a/b
    print(c)

except ValueError:
    print("only numbers are allowed,please check it")

except ZeroDivisionError:
    print("second number cannot be zero")

except:
    print("some error occured, please contact admin@test.com")

finally:
    print("\n\n\n\n designed by: Lavanya")

input()
