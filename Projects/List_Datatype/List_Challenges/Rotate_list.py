#rotate a given list by n places
n=2
L1=[10,20,30,40,50,60,70]
L2=[]
counter=0

while counter<n:
    L2.append(L1[0])
    L1.pop(0)
    counter+=1

L1.extend(L2)
print(L1)

#other solution
L1=[10,20,30,40,50,60,70]
L2=L1[n:]+L1[:n]
print(L2)