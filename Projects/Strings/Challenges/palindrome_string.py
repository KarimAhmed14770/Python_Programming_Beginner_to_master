#if the string is reversed and it is still the same this is called palindrome
given_string=input('enter a string: ')
given_string_=given_string.casefold()
given_string_=given_string_.replace(' ','')
reversed_string=given_string_[::-1]
if(given_string_==reversed_string):
    print(f'{given_string} is a palindrome')
else:
    print(f'{given_string} is not a palindrome')