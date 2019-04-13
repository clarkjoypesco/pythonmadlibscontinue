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


