
#!/usr/bin/env python


import os
import sys
import pprint
import random
import twitter


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    word_list1 = corpus.split()
    word_list = [x.strip('"') for x in word_list1] #get rid of quotes
    
    word_dict = {}
    for i in range(2,len(word_list)):
        #print word_list[i-2:i], word_list[i]
        bgram = word_list[i-2:i]
        link = word_list[i]
        if not word_dict.get((bgram[0],bgram[1])):
            word_dict[bgram[0],bgram[1]] = [link] # this makes the key a tuple
            #word_dict[bgram[0] + " " + bgram[1]] = [link] # this makes the key a string
        else:
            word_dict[bgram[0],bgram[1]] += [link] # this makes the key a tuple
            #word_dict[bgram[0] + " " + bgram[1]] += [link]    

    #pprint.pprint(word_dict)
    return word_dict

def pick_random_key(chains):
    random_key = random.sample(chains.keys(), 1)
    #we want a capitalized word here, pick until this part is true
    while not random_key[0][0].istitle():
        random_key = random.sample(chains.keys(), 1)
    return random_key

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    random_key = pick_random_key(chains)
    #print "first random key:", random_key
    sentence = [random_key[0][0], random_key[0][1]]
    while chains.get(random_key[0]) and len(" ".join(sentence)) < 135:
        pick_value = chains[random_key[0]][random.randint(0, len(chains[random_key[0]])-1)]
        #print "pick value:", pick_value
        #make new bigram with y value from random_key and pick_value 
        
        if pick_value.lower() in  ["a", "the", "and", "an", "of"] and len(" ".join(sentence)) > 130:
            print "TRUE"
            break
        else:
            sentence.append(pick_value.lower())
            #print pick_value

        result =  "\n" +  " ".join(sentence) #+ random.choice(endings)
        if result[-1].isalnum():
            result += "."
        random_key = [(random_key[0][1], pick_value)]
        #print "new random key:", random_key
   
    return result        

def main():
    #args = sys.argv
    f = open("../short.txt")
    input_text = f.read()
    #print input_text

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()