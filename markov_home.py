#!/usr/bin/env python

import os
import sys
import pprint
import random
import twitter

def twitter_stuff(sentence):

#TODO use a safer method than won't crash if environment variable not there

    cs = os.environ.get('TWITTER_API_SECRET')
    ck = os.environ.get('TWITTER_API_KEY')
    ts = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    tk = os.environ.get('TWITTER_ACCESS_TOKEN')

    api = twitter.Api(consumer_key=ck,consumer_secret=cs,access_token_key=tk,access_token_secret=ts)
    status = api.PostUpdate(sentence)
    print status

    return


def make_chains(text):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    text_list = text.split()
    text_dict = {}

    for i in range(2,len(text_list)):
        bgram1 = text_list[i-2].strip('\"')
        bgram2 = text_list[i-1].strip('\"')
        value = text_list[i].strip('\"')
        if not text_dict.get((bgram1, bgram2)):
            text_dict[bgram1, bgram2] = [value]
        else:
            text_dict[bgram1, bgram2] += [value]
    #pprint.pprint(text_dict)
    return text_dict

def pick_first_random_key(chains):
    random_key = (random.sample(chains.keys(), 1))
    while not random_key[0][0].istitle():
        random_key = (random.sample(chains.keys(), 1))
    return random_key        


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #get random key from dictionary and add it to list
    random_key = pick_first_random_key(chains)
    sentence = [random_key[0][0],random_key[0][1]]
    endings = [" in between the sheets!", " in betwixt the sheets where you read Nicholas Sparks every night!", " in the sack!", " in your black satin sheets, dog!", " in between your TJ MAXX discount sheets!", \
    " in between your STAR WARS bedsheets!", " in between the sheets of the bed in your parents basement!", " in between the sheets where you listen to R Kelly, playa!", \
    " in between the sheets where you write in your diary, Taylor Swift!"]

    while chains.get(random_key[0]) and len(" ".join(sentence)) < 135: #while our key exists in the dict
        pick_value = chains[random_key[0]][random.randint(0, len(chains[random_key[0]])-1)]
        #make new bigram with y value from random_key and pick_value 
        
        if pick_value.lower() in  ["a", "the", "and", "an"] and len(sentence) > 130:
            print pick_value
            break
        else:
            sentence.append(pick_value)

        result =  "\n" +  " ".join(sentence) + random.choice(endings)
        if result[-1].isalnum():
            result += "."
        random_key = [(random_key[0][1], pick_value)]
   
    return result


def main():
    #args = sys.argv[1]
    script, filename  = sys.argv 
    # Change this to read input_text from a file
    f = open(filename)
    input_text = f.read()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

    #twitter_live = os.environ.get('TWITTER_LIVE')
    

    
    # if twitter_live == 'YES':
    #     #print 'do we really want a live tweet?'
    twitter_stuff(random_text)
    # else:
    #     print random_text

if __name__ == "__main__":
    main()