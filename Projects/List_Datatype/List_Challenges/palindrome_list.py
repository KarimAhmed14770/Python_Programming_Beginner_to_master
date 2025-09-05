#given a list if it is the same if read from right to left then it is palindrome
#fiven a list check if it is palindrome

def palindrome_check(L1):
    length=len(L1)
    palindrome=True
    counter=0
    while counter<length:
        if L1[counter]!=L1[length-1-counter]:
            palindrome=False
        counter+=1

    return palindrome

L1=[1,2,3,3,2,1]
L2=[10,30,50,80,90,90,80,50,30,10]
L3=[1,2,4,5,6,7]
print(palindrome_check(L1))
print(palindrome_check(L2))
print(palindrome_check(L3))