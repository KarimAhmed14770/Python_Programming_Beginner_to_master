#getting all possible arrangements of a list
#to know the number of permutations nPr=(n!)/(n-r)! n is total number of elements,
# r is number of places
#combinations mean all possible selections nCr=(n!)/(n-r)!*r!
#itertools module
import itertools as itr
from itertools import repeat

L=list("Python")
#itertools.permutations(iterable,r=none)
Permutations=itr.permutations(L) #this returns a permutations object
Permutations=list(Permutations)#this converts the permutation object to a list
for p in Permutations:
    print(p)

Permutations=itr.permutations(L,r=2) #this returns a permutations object
Permutations=list(Permutations)
for p in Permutations:
    print(p)

Combinations=itr.combinations(L,r=6) #this returns a combination object
Combinations=list(Combinations)
for c in Combinations:
    print(c)

Combinations=itr.combinations(L,r=2) #this returns a combination object
Combinations=list(Combinations)
for c in Combinations:
    print(c)


#itertools.product(*iterables,repeat=1),returns the cartesian product of iterables
L=['A','B','C']
L1=[1,2,3]
product=itr.product(L,L1)
product=list(product)
for p in product:
    print(p)

product=itr.product(L,L1,repeat=2)
product=list(product)
for p in product:
    print(p)



