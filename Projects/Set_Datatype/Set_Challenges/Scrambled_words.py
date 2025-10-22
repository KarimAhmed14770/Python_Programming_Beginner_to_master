word_set = {'plea', 'medical', 'listen', 'leap', 'decimal', 'silent', 'pale', 'enlist'}

unique_sets=[]
result=[]
counter=0
for word in word_set:
    unique_set=set(word)
    if(unique_set not in unique_sets):
        unique_sets.append(unique_set)
result=[None]*len(unique_sets) #adjusting the size
for word in word_set:
    unique_set = set(word)
    while counter<len(unique_sets):
        if unique_set==unique_sets[counter]:
            if(result[counter]==None):
                result[counter]=[word]
                counter=0
                break
            else:
                result[counter].append(word)
                counter=0
                break
        counter+=1

print(result)

##this was very bad solution
#much better solution
def get_anagrams(words):
    anagram_groups={}#the result will be returned in dictionary
    for word in words:
        key=tuple(sorted(word))#the key will be the sorted letters for each word
        anagram_groups.setdefault(key,[]).append(word)

    return list(anagram_groups.values())


result=get_anagrams(word_set)
print(result)
