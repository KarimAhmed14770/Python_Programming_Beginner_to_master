#given two texts we need to check if there is a plagiarism. we calculate the  percent by
#getting common words, and unique words in both texts and dividing common words by unique words
import re

str1 = ('Time is the most valuable thing we have,'
        ' and once lost, it never returns.')
str2 = ("We never get time back once it's "
    "gone—it's truly the most valuable resource.")
#we will get common or unique words using regular expressions

#first i will get unique words from each text
str1_unique=set(re.findall(r"\b[a-z]+\b",str1.lower()))
#print(str1_unique,len(str1_unique))
str2_unique=set(re.findall(r"\b[a-z]+\b",str2.lower()))
#print(str2_unique,len(str2_unique))

common_words=str1_unique.intersection(str2_unique)
#print(common_words,len(common_words))
all_words=str1_unique.union(str2_unique)
#print(all_words,len(all_words))

plagiarism_percent=(len(common_words)/len(all_words))*100
print(plagiarism_percent)