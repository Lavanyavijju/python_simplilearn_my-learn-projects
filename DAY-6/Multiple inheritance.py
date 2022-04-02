class Algebra:
    def add(a,b):
        return a+b
    def mul(a,b):
        return a*b
class Trigonometry:
    def sin0():
        return 0
    def cos0():
        return 1
class TotalMaths(Algebra,Trigonometry):
    def sub(a,b):
        return a-b
    def div(a,b):
        return a/b

print(TotalMaths.sin0())
print(TotalMaths.add(5,7))
    
