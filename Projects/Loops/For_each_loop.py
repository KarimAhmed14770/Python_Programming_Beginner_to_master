#for each loop:
#it is the most comon loop in python programing
#it is given a sequence of elements and it iterates for each element
#syntax
#for var_name in sequence:
#       Body
list1=[10,20,30,40,50]

for i in list1:
    print(i)

#range() function: range(start=0,stop,step=1)
#the range function produces a sequence with its start 0 by default, could be changed
#stop ust be passed
#step is 1 by default and it could e changed
#it doesn't reach the stop value it terminates before the stop value
#the last element =stop value- step
for i in range(10):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(10,0,-1):
    print(i)

#for with strings
for i in 'Karim':
    print(i,sep=',',end=' ')