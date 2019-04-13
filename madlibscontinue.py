# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?

import random
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

list1 = list1 + [5, 6]
list2.append([5, 6])

# to check, you can print them out using the print statements below.

print "showing list1 and list2:"
print list1
print list2


# What is the difference between these two pieces of code?
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]


def proc(mylist):
    mylist = mylist + [6, 7]


def proc2(mylist):
    mylist.append(6)
    mylist.append(7)

# Can you explain the results given by the print statements below?


print "demonstrating proc"
print list1     # prints [1,2,3,4,5]

proc(list1)  # adding list1 = [1,2,3,4,5] to [6,7] => [1,2,3,4,5,6,7]
print list1  # print [1,2,3,4,5]

print
print "demonstrating proc2"
print list2  # prints [1,2,3,4,5]
# appending list2 = [1,2,3,4,5] with (6) and then (7) => [1,2,3,4,5,6,7]
proc2(list2)
print list2  # so this should print [1,2,3,4,5,6,7]

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1, 2, 3, 4, 5]


def proc3(mylist):
    mylist += [6, 7]
    return mylist


print proc3(list3)

# Does this behave like list1 = list1 + [6,7] or list2.append([6,7])? Write a
# procedure, proc3 similar to proc and proc2, but for +=.

# ==========================================================================

# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data

# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.

# To create a random integer from 0 to 10, we first import the
# "random" module


# We then print a random integer using the random.randint(start, end) function
print "Random number generated: " + str(random.randint(0, 10))

# Remember that if we want to concatenate a string and a number, we need to convert the
# integer into a string using the str() function

# We now want to create a list filled with random numbers. The list should be
# of length 20


# Write code here and use a while loop to populate this list of random integers. A crucial
# function that will help you is to use the append() method to add elements to a list.
random_list = []
list_length = 20

i = 0
while i < list_length:
    random_list.append(random.randint(0, 10))
    i += 1

# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]

print random_list

# alternative code by answer
random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0, 10))

#================================================================================
# Now, we want to ask ourselves the question: How many occurrences of
# the number 9 appear in our randomly made list?
#
# For example, if we have a list: [2,8,9,9,4,5,9], we want to figure out
# how to loop through the list and count the number of occurrences of the
# number 9. In the example list above, the number 9 occurs three times.


# 1. Create random list of integers using while loop
random_list = []
list_length = 20
count = 0
while len(random_list) < list_length:
    random_list.append(random.randint(0, 10))

# Write code here to loop through the list and count all occurrences
# of the number 9. Note that `if` statements and `while` loops will help you solve
# this problem.
index = 0
while index < len(random_list):
        if random_list[index] == 9:
                count +=1
        index +=1

# Test: If the `while` loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
print random_list
print count


#============================================================================

# Great! We now want to create a new list that contains the counts
# of all occurrances of every number seen in the randomly generated 
# list. That means we want counts of all occurrences of all numbers
# from 0 through 10 in our randomly generated list.

# Let's store our counts in a list of length 11 
# with zeros filled in.

# We can multiply a list construct to create a list with the same
# elements n number of times.
count_list = [0] * 11

# Check that we have a list of length 11 with all 0 elements
print count_list

# We use this list to store our count of numbers 0 to 10 - take note 
# that total numbers 0 to 10 is 11. We can use the index number of
# each element to refer to the count of our target
# number. Our target number is actually the index of the list.
# For example, assume count_list looks like this:

count_list = [1,2,3,2,2,1,1,2,3,1,2]

# Let's print out the occurrences for the numbers 0, 4, 5, and 6
print count_list[0]
print count_list[4]
print count_list[5]
print count_list[6]

# Therefore, for our output, we want a count_list that looks like:
# [1,2,3,2,2,1,1,2,3,1,2]

# Here's our code that we coded before

import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))
# --------------------------------------------------------------------

# Initialize count_list for every integer between 0 and 10. 
# A number will correspond to an index of this count_list
# Therefore if we see that there are 3 occurrences of the number 4, 
# we assign count_list[4] = 3, if there are 5 occurrences of the 
# number 6, we assign count_list[6] = 5

count_list = [0] * 11
i= 0
count = 0
#Write code here to loop through every number in random_list and
#update count_list appropriately
while i < len(count_list):
        count_list[i] = random_list[i]
        #0
        j = 0
        while j < len(random_list):
                if count_list[i] == random_list[j]:
                        count +=1
                j+=1
        count_list[i] = count
        count = 0
    
        i+=1
     





# Check the list we created
print random_list
print count_list
# If we coded everything correctly, the sum of all of the numbers 
# in count_list should be 20
print sum(count_list)