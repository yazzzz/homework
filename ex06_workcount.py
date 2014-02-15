#!/usr/bin/python

import pprint

f = open("test.txt")
filetext = f.read().strip().lower()
f.close()

word_list = filetext.split()

#get rid of extra chars
clean_word_list = [x.strip(",.:?!#*()[]%@$^&") for x in word_list]
#print clean_word_list

#setup the dictionary with an entry for each word
word_dict = {}
for word in clean_word_list:
    if not word_dict.get(word): #if word is not in the dict, add it
        word_dict[word] = 1
    else: 
        word_dict[word] += 1 #if word is there, increment the value

#this is the dict sorted by alphabet
print "1. PRINTING KEYS SORTED ALPHABETICALLY"
pprint.pprint(word_dict)
"""
{'aero': 9,
 'aim': 7,
 'anddd': 10,
 'apple': 10,
 'band': 9,
 'book': 2,
 'cat': 10,
 'pie': 2,
 'zappo': 7}
 """
#---------------------

#setup a dict that is count, word instead of word, count
value_dict = {}
for key, value in word_dict.items():
    value_dict[value] = []
#pprint.pprint(value_dict)
"""{2: [], 7: [], 9: [], 10: []}"""

for key, value in word_dict.items():
    value_dict[value] += [key]
"""
{2: ['pie', 'book'],
 7: ['aim', 'zappo'],
 9: ['aero', 'band'],
 10: ['apple', 'anddd', 'cat']}
 """

#---------------------
print "\n3. SORTED BY VALUE, ALPHABETICALLY WITHIN EACH VALUE"
for key in sorted(value_dict, reverse=True):
    print (key, sorted(value_dict[key]))
    #sorted_dict[key] = sorted(value_dict[key])
"""
(10, ['anddd', 'apple', 'cat'])
(9, ['aero', 'band'])
(7, ['aim', 'zappo'])
(2, ['book', 'pie'])
"""
