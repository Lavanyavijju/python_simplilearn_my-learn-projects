name=input("Enter your name:")
score=0
print("Q1. Capital of India:")
print("1.Hyderabad 2.NewDelhi 3.Colombo 4.Canberra")
ans=int(input("Enter your choice:"))
if(ans==2):
    score=score+20

print("Q2. Capital of Australia:")
print("1.Canberra 2.NewDelhi 3.Colombo 4.Canberra")
ans=int(input("Enter your choice:"))
if(ans==1):
    score=score+20

print("Q3. Capital of Bangladesh:")
print("1.Canberra 2.NewDelhi 3.Dhaka 4.Canberra")
ans=int(input("Enter your choice:"))
if(ans==3):
    score=score+20

print("Q4. Capital of USA:")
print("1.Canberra 2.NewDelhi 3.Dhaka 4.Washington DC")
ans=int(input("Enter your choice:"))
if(ans==4):
    score=score+20

print("Q5. Capital of Srilanka:")
print("1.Canberra 2.NewDelhi 3.Colombo 4.Washington DC")
ans=int(input("Enter your choice:"))
if(ans==3):
    score=score+20

print("your score is:")
print(score)

input()
