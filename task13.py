#!/usr/bin/python
'''

'''
import math
import pdb

def round(inp): #inp is a number
    """round a number up or down by checking if it's over 0.5"""
    base = int(inp)
    if inp - base >= 0.5:
        return base+1
    else:
        return base
    
#print round(13.3)

def count_lines(inp): #inp is a string of text"
    """count the number of lines of text"""
    if not inp:
        return 40000
    num = 1
    for c in inp:
        if c == "\n":
           num  += 1    
    return num

#print count_lines("asdas\ndkfjdklf\nkjdkfjd\nkjkdfj")

def pythagorean(a, b):
    """compute length of triagle side given a and b using pythagorean theorem"""
    c = a * a + b * b
    return math.sqrt(c)

#print pythagorean(3,4)

def reverse(list1):
    """reverse the list"""
    size = len(list1)
    for i in range(len(list1)/2):
        print "list1[i]", list1[i]
        temp = list1[i]
        print "temp", temp
        list1[i] = list1[size-i-1]
        print "list1[i]", list1[i], "list1[size-i-1]", list1[size-i-1]
        list1[size-i-1] = temp
        
    return list1

#print reverse(["g","l","a","z","b"])    

def count_words():
    """ count how many times each word appears"""
    #inp = open("../green.txt")
    #ws = inp.read().split()
    word_list = ['Would', 'you,', 'could', 'you', 'in', 'a', 'house', 'Would', 'you,', 'could', 'you', 'with', 'a', 'mouse', 'Would', 'you,']
    hdict = dict()
    for word in word_list:
        num = hdict.get(word, 0)
        num += 1
        hdict[word] = num
        #print hdict[word], word
    
    for k, v in hdict.iteritems():
        print "%s:%d"%(k, v)

#print count_words()

def copy_lowest(inp):
    """ takes the lowest value and copies it to the left"""
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                tmp = inp[i]
                inp[i] = inp[i+1]
                inp[i+1] = inp[i]
                swapped = True
    return inp

print copy_lowest([4,1,0,3])
print copy_lowest([4,3,2,1])