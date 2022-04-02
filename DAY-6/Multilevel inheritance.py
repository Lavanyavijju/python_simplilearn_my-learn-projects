class Algebra:
    def add(a,b):
        return a+b
class TotalMaths(Algebra):
    def mul(a,b):
        return a*b
class AllSubjects(TotalMaths):
    def div(a,b):
        return a/b

print(AllSubjects.add(5,6))
print(AllSubjects.mul(9,8))
print(AllSubjects.div(6,3))
        
