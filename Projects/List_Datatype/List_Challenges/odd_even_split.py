#given a list separate odd elements in a list and even elements in a list

L=[1,4,5,80,54,32,6,32,31,45,6,89,88,90,32,43,54,56,76,85,42,31,99]
odd_list=[]
even_list=[]

for x in L:
    if x%2==0:
        even_list.append(x)
    else:
        odd_list.append(x)

print(even_list)
print(odd_list)