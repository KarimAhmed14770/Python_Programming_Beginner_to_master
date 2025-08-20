#challenge 1 factorial of a given number
n=int(input('enter a number: '))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(f"factorial of {n} is: {factorial}")

#challenge 2 the fibonnaci series of a number
'''The Fibonacci series of a number isn't a direct concept. 
Instead, a Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones,
 starting from 0 and 1.
  The "number" you provide would typically be the length of the series you want to generate 
  or the index of a specific Fibonacci number you want to find.

What is the Fibonacci Series?
The sequence typically starts:
0,1,1,2,3,5,8,13,21,34,...'''

fib=0
fib_1=0
fib_2=1
counter=0
index_=int(input("enter the index to calculate fibonnaci series: "))
for i in range(index_+1):
    if(i==0):
        fib_2=0
    elif(i==1):
        fib_1=1
    else:
        fib=fib_1+fib_2
        fib_2 = fib_1
        fib_1=fib

print(fib)

#nested loops challenges (patterns)
#pattern 1 square of *
rows=int(input('enter number of rows: '))
for i in range(rows):
    for j in range(rows):
        print("* ",end='')
    print('')
#pattern 2:triangle
rows=int(input('enter number of rows: '))
counter=0
for i in range(1,rows+1):
    for j in range(rows):
        if(j<i):
            print("* ",end='')
    print("")
