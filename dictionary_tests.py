#!/usr/bin/python

d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}


""" 1.  count how many times each letter appears in the 2 dicts """

countletter_dict = {}
for letter in d1.keys() + d2.keys():
    if not countletter_dict.get(letter): #if word is not in the dict, add it
        countletter_dict[letter] = 1
    else:
        countletter_dict[letter] += 1 #if word is there, increment the value

print countletter_dict

""" 2a. make an dict with empty lists as values """

letter_dict = {}
for letter in d1.keys() + d2.keys():
    if not letter_dict.get(letter): #if word is not in the dict, add it
        letter_dict[letter] = []

print letter_dict

""" 2b. append values from d1 and d2 into letter_dict"""

for key, value in d1.items() + d2.items():
    letter_dict[key] += [value]

print letter_dict

#############################################################################

""" 3a. add the values from d1 and d2 into letter_dict"""


letter2_dict = {}
for letter in d1.keys() + d2.keys():
    if not letter2_dict.get(letter): #if word is not in the dict, add it
        letter2_dict[letter] = 0

print letter2_dict

""" 3b. append values from d1 and d2 into letter_dict"""

for key, value in d1.items() + d2.items():
    letter2_dict[key] += value

print letter2_dict

