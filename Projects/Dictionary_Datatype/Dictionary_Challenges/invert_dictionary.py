#you will be give a dictionary and it is required to make the keys values and vice versa



def invert_dict(d):
    inverted={}
    for x,y in d.items():
        if y in inverted:
            inverted[y].append((x))
        else:
            inverted[y]=[x]
    return inverted


d1={1:"One",2:"Two",3:"Three",4:'One'}

d2=invert_dict(d1)
print(d2)