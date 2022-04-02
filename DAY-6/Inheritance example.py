class Algebra:
    def add(a,b):
        return a+b
    def mul(a,b):
        return a*b
class TotalMaths(Algebra):
    def sub(a,b):
        return a-b
    def div(a,b):
        return a/b

print(TotalMaths.sub(9,8))
print(TotalMaths.div(8,2))
        
