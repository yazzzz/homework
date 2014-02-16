#!/usr/bin/python


""" Multiply all the elements in a list"""
def multiply_list1(l): # WORKS
    if len(l) == 1:
        return l.pop()
    else:
        return l.pop() * multiply_list(l)

def multiply_list2(l): # WORKS
    if len(l) == 1:
        return l[-1]
    else:
        print l[-1], l[:-1]
        return l[-1] * multiply_list(l[:-1])

def multiply_list(l): # from christian, fixed
    if l == []:
        return 1

    return l[0] * multiply_list(l[1:])

#print multiply_list([1, 2, 3, 4, 5])

###################################################################################################

"""Return the factorial of n """
def factorial(n): #verbose version
    if n <= 1: #can be 0 but 1 will stop sooner
        return 1
    else:
        print n, n-1
        result = factorial(n - 1) * n
        print result, n
    return result

def factorial2(n): #short version
    if n == 0: 
        return 1 #don't murder ever
    return factorial(n - 1) * n ## don't murder me

def factorial3(n): #non recursion version
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

#print factorial(5)

###################################################################################################
""" Count the number of elements in the list l """
def count_list2(l): #WORKS
    if len(l) == 1:
        return 1
    else:
        print l[:-1]
        return count_list(l[:-1]) + 1


def count_list(l): # from christian, fixed
    if l == []:
        return 0

    return 1 + count_list(l[1:])

#print count_list([1, 2, 3, 4, 5, 6])

###################################################################################################
""" Sum all of the elements in a list """
def sum_list1(l):
    if len(l) == 1:
        return l.pop()
    else:
        return l.pop() + sum_list(l)

def sum_list2(l):
    if len(l) == 1:
        return l[-1]
    else:
        print l[-1]
        return l[-1] + sum_list(l[:-1])

def sum_list(l): #from christian
    if l == []:
        return 0

    return l[0] + sum_list(l[1:])

#print sum_list([1, 2, 3, 4, 5])

###################################################################################################
""" Reverse a list without slicing or loops """
def reverse1(l):
    if len(l) == 1:
        return l
    else:
        print l
        return [l.pop(0)] + reverse(l) #pop(0) is the first elem of the list


def reverse2(l):
    if len(l) <= 1:
        return l
    else:
        print [l[-1]] + l[:-1]
        return [l[-1]] + reverse(l[:-1])


def reverse3(l):
    counter = 0
    if len(l) <= 1:
        return l
    else:
        counter += 1
        print counter, l[1:], [l[0]]
        return reverse(l[1:]) + [l[0]]

def reverse(l): #from christian, similar to prev
    if l == []:
        return []

    return reverse(l[1:]) + [ l[0] ] # We wrap l[0] in extra brackets to force it to extend the first list

#print reverse([1,2,3,4])

###################################################################################################
""" Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)"""
def fibonacci(n): #WORKS
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci1(n): #from christian
    if n <= 1:
        return 1

    return fibonacci(n-2) + fibonacci(n-1)

#print fibonacci(8)

###################################################################################################
"""Finds the item i in the list l.... RECURSIVELY
yaz is totally confused on if 'item i' means the index or the value
find the value and return it if it exists, otherwise
#        return None if not in the list"""

def find(i, l):
    if i == l[0]:
        return l[0]
    else:
        l.pop(0)
        return find(l, i-1)
    
def find2(i, l): # from christian
    if l == []:
        return None

    if l[0] == i:
        return i

    return find(i, l[1:]) 

#print find(5, [5, 2, 1, 4, 3, 6])

#print find('Jan',['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'])
###################################################################################################
""" Determines if a string is a palindrome"""
def palindrome1(some_string): #WORKS
    if len(some_string) <= 1:
        return True
    else:
        first_value = some_string[0]
        last_value = some_string[-1]
        if first_value != last_value:
            return False
        else:
            return palindrome(some_string[1:-1])

def palindrome(some_string):
    if len(some_string) <= 1:
        return True

    return (some_string[0] == some_string[-1]) and palindrome(some_string[1:-1])

#print palindrome("toot")    

###################################################################################################
""" Given the width and height of a sheet of paper, and the number of times to fold it, 
 return the final dimensions of the sheet as a tuple. Assume that you always 
 fold in half along the longest edge of the sheet. """
def fold_paper1(width, height, folds):
    if folds == 0:
        return (width, height)
    else:
        bigger = max(width, height)
        if width == bigger or width == height:
            return fold_paper(width/2.0, height, folds-1)
        else:
            return fold_paper(width, height/2.0, folds-1)

def fold_paper(width, height, folds): #from christian, fixed
    if folds == 0:
        return (width, height)

    if width < height:
        return fold_paper(width, height/2.0, folds-1)
    else:
        return fold_paper(width/2.0, height, folds-1)

#print fold_paper(18,6,3)


###################################################################################################
""" Count up
Print all the numbers from 0(n?) to target """
def count_up(n, target): # WORKS
    if n == target:
        print n
    else:
        print n
        count_up(n + 1, target)

def count_up(target, n): #from christian
    print n
    if n == target:
        return
    count_up(target, n+1)

#count_up(4, 12)