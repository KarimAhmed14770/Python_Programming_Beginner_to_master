# there are 2 loops in python programming while and for each loops
#while loop
#syntax:
'''while condition:
        Body
'''
#1) counter concept
counter=0
while counter<10:
    counter+=1
    print(counter)

print("\n")
#to print multiples of a number
counter=0
n=3
while counter<10:
    counter+=1
    print(counter*n)

#2) to count the digits of a number
n=25789
digits_count=0
while n>0:
    digits_count+=1
    n//=10

print(f"digits_count: {digits_count}")

#find the sum of digits of a number
n=25789
sum_=0
while n>0:
    sum_+=(n%10)
    n//=10
print(f"sum is: {sum_}")

#3 reverse a number
n=25789
rev=0
rem=0
while n>0:
    rem=n%10
    rev=rem+(rev*10)
    n//=10

print(f"the reverse is: {rev}")

#4 find max and min element
list1=[10,20,30,50,100,21,444,2,1,-60]
counter=0
max_=float('-inf') #this is how to represent -infinity
min_=float('inf')  #this is how to represent  infinity
while counter<len(list1):
    if(list1[counter]>max_):
        max_=list1[counter]
    if(list1[counter]<min_):
        min_=list1[counter]
    counter+=1
print(f"max is: {max_}\tmin is: {min_}")

