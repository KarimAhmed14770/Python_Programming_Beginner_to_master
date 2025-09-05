#you have a list that contains duplicate, remove duplicates
L1=[10,20,30,10,60,30,20,20,60,50,70,30]
L2=[]
counter=0
for x in L1:
    if x not in L2:
        L2.append(x)
print(L2)

#or using sets
s=set(L1)
L2=list(s)
print(L2)