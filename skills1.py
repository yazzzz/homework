#!/usr/bin/python

# Things you should be able to do.


some_list = [1,21,2,5,6,7,9,12,13]
numbers = [1,21,2,5,6,7,9,12,13]
word_list = ['cat', 'goes', 'meow,', 'dog', 'goes', 'woof,', 'seal', 'goes', 'ow', 'what', 'does', 'the', 'fox', 'say']

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    return [x for x in some_list if x % 2 != 0]

print all_odd(some_list)

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    return [x for x in some_list if x % 2 == 0]

print all_even(some_list)


# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    # result = []
    # for i in word_list:
    #     if len(i) >= 4:
    #         result.append(i)
    # return result
    return [x for x in word_list if len(x) >= 4]

print long_words(word_list)


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):    
    return sorted(some_list)[0]
    #return min(some_list)


# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return sorted(some_list)[-1]
    #return max(some_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    return [float(x)/2 for x in some_list]

print halvesies(some_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return [len(x) for x in some_list]

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    return reduce(lambda x,y: x + y, numbers)
    # result = 0
    # for i in numbers:
    #     result += i
    # return result

print sum_numbers(some_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    return reduce(lambda x,y: x * y, numbers)

print mult_numbers(numbers)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    return reduce(lambda x,y: x + y, word_list)
    # result = ""
    # for i in word_list:
    #     result = result + i
    # return result

print join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    #return sum(numbers)/len(numbers)
    return reduce(lambda x,y: x + y, numbers)/float(len(numbers))    

print average(numbers)

