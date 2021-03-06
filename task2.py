#!/usr/bin/python


"""1.
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]
#print l[::-1]

"""2.
Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""
d = {"q": 5, "m": 3, "z":2, "a": 10}

# for k,v in sorted(d.items()):
#     print "%s, %d" % (k, v)


"""3.
Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""
l1 = [1, 3, 4, 6, 8, 10]
l2 = [93, 2, 23, 77, 66]

#print sorted(list(set(l1+l2)))

"""4.
Given the string s, split it into two strings, s2 and s3, s2 containing the first 5 letters of the string, and s3 containing 
the remaining letters.

eg:
    s1 = "Hello there"
    s2 = "Hello"
    s3 = " there"

"""
s = "Hi there, my name is Slim"

s2 = s[:5]
s3 = s[5:]

#print s2, s3

"""
5. Given the string s, excise characters 6 through 12, inclusive
eg:
    s = "Hello, good sir"
    becomes 
    s = "Hello sir"
"""
#s = "hello, good sir"
s = "Hi there, my name is Slim"
#print s
#print s[:5] + s[11:]

"""6.
Given the string s, produce a list composed of all the single characters from the original string
eg:
    s = "Hello"
    becomes
    l = {"H", "e", "l", "l", "o"}
"""
s = "Hi there, my name is Slim"

#print [x for x in s]
#print list(s)

"""7.
Given the list l composed of tuples, sort the list by the second item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]
"""
l = [(1,2), (3,1), (17, 35), (81,20)]

#print sorted(l, key=lambda x: x[1])

"""XXX 8.
Given two dictionaries, d1 and d2, update the contents of d1 with the contents of d2, overwriting any existing keys
eg:
    d1 = {"a":1, "b":2}
    d2 = {"a":3, "c":4}

    becomes

    d1 = {"a":3, "b":2, "c":4}
"""
d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}

#overwrite keys
#print d1
d1.update(d2)
#print d1




"""9. Given two dictionaries, d1 and d2, merge the contents of d1 with the contents of d2, adding to the values of existing keys
eg:
    d1 = {"a": 1, "b":2}
    d2 = {"a": 3, "d": 4}

    becomes

    d1 = {"a": 4, "b":2, "d":4}

"""
d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}
d3 = {}
d4 = {}

allkeys = d1.keys() + d2.keys()
uniquekeys = set(allkeys)

for item in uniquekeys:
    #print d1.get(item, 0), d2.get(item, 0)
    d3[item] = d1.get(item, 0) + d2.get(item, 0)

print "d3",d3





#10.
s = """
Given a multiline string 's', print each line along with the line number

eg:
    mystr = "Sorry,\nMy people need me\nI must go"

    prints

    1. Sorry,
    2. My people need me
    3. I must go.

"""

def lineNumbers(string1):
    list1 = string1.split("\n")
    for i,v in enumerate(list1):
        print str(i+1) + ". " + v
        #or 
        #print "%d. %s" % (i+1, v.strip())


#lineNumbers("Sorry,\nMy people need me\nI must go")


"""11.
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""

def title(my_title):
    result = ""
    for i in my_title.split():
        result += i.title() + " "
    return result.strip()


#print title("a tale of two cities")

"""12.
Write the following two functions
    c_to_f(float) -> float
    f_to_c(float) -> float

c_to_f should convert a temperature in celsius to fahrenheit, and f_to_c should do the opposite
"""

def c_to_f(temp):
    """37C x  9/5 + 32 = 98.6F"""
    return temp * (9.0/5) + 32

#print c_to_f(37)


def f_to_c(temp):
    """(98.6F  -  32)  x  5/9 = 37C"""
    return (temp - 32) * (5.0/9)

#print f_to_c(98.6)