name=input("Enter student name:")
isFound=False

f1=open("scores.txt","r")

data=f1.readlines()

for d in data:
    row=d.split(",")
    if(row[0]==name):
        print("score=",row[1])
        isFound=True
        break
if(isFound==False):
    print("student not found")
