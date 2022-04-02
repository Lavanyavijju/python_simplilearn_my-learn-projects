#printing 1 to 10 and 10 to 1 continuosly
i=1
order=1
while(True):
    print(i,end="")
    if(i==10):
        order=-1
    if(i==1):
        order=1
    i=i+order
