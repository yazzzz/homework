import pprint


inputfile = open("test.txt")
filecontents = inputfile.read()

before_wordlist = filecontents.lower().split()

# Separating file into words
wordlist = []
for word in before_wordlist:
    newword = word.strip(",.:?!#*()[]%@$^&")
    wordlist.append(newword)

word_dict = {}

#go thru wordlist, if increment the value if the word exists,
#else if word is not in the dict, add it as a key, default value of 1

for word in wordlist:
    if word in word_dict:
        word_dict[word]+= 1
    else:
        #word_dict.setdefault(word,1)
        word_dict[word] = 1

print "1. PRINTING KEYS SORTED ALPHABETICALLY"
pprint.pprint(word_dict)


print "\n3. SORTED BY VALUE, ALPHABETICALLY WITHIN EACH VALUE"
word_dict_values_as_keys = {}

for number in sorted(word_dict.values(), reverse=True):
    if number not in word_dict_values_as_keys:
        word_dict_values_as_keys[number] = []

for word, number in sorted(word_dict.items()):
    word_dict_values_as_keys[number].append(word)

for number in sorted(word_dict_values_as_keys, reverse=True):
    print (number, word_dict_values_as_keys[number])







