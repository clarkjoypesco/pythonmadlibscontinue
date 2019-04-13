# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6]
list2.append([5, 6])

# to check, you can print them out using the print statements below.

print "showing list1 and list2:"
print list1
print list2


# What is the difference between these two pieces of code?
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

def proc(mylist):
    mylist = mylist + [6, 7]
  
   

def proc2(mylist):
    mylist.append(6)
    mylist.append(7)

# Can you explain the results given by the print statements below?

print "demonstrating proc"
print list1     # prints [1,2,3,4,5]

proc(list1) # adding list1 = [1,2,3,4,5] to [6,7] => [1,2,3,4,5,6,7]
print list1  # print [1,2,3,4,5]

print
print "demonstrating proc2"
print list2  # prints [1,2,3,4,5]
proc2(list2) # appending list2 = [1,2,3,4,5] with (6) and then (7) => [1,2,3,4,5,6,7]
print list2 # so this should print [1,2,3,4,5,6,7]

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4,5]

def proc3(mylist):
    mylist += [6, 7]
    return mylist

print proc3(list3)

# Does this behave like list1 = list1 + [6,7] or list2.append([6,7])? Write a
# procedure, proc3 similar to proc and proc2, but for +=.

#==========================================================================

# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data

# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.

# To create a random integer from 0 to 10, we first import the 
# "random" module

import random

# We then print a random integer using the random.randint(start, end) function
print "Random number generated: " + str(random.randint(0,10))

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
        random_list.append(random.randint(0,10))
        i+=1

# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]

print random_list


