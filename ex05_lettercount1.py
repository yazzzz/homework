#!/usr/bin/python

""" count the number of each letter"""

f = open("short.txt")
filetext = f.read()
f.close()


fileletters  = ''.join(x for x in filetext if x.isalnum() and not x.isdigit()).lower()
print fileletters
#letters = sorted("abaskdfdsfklriuqeirqeiwrpoqwi")
letters = sorted(fileletters)

result = [0] * 26

for letter in letters: # got thru the list of letters
    # find out where this letter should land in our list of 26 zeros that represent the alphabet
    # ascii value of the letter a is 97 so we subtract 97 and get 0
    letter_index = ord(letter) - 97 
    # on the first run you set the location of the letter
    #print letter, letter_index
    result[letter_index] += 1

print result

for i in range(len(result)):
    print result[i], chr(i + 97)