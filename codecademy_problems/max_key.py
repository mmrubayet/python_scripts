### Problem

'''
Write a function named max_key that takes a dictionary named
my_dictionary as a parameter. The function should return the key
associated with the largest value in the dictionary.

'''



### Solution

def max_key(my):
  mk = list(my.keys())[0]
  for k in my.keys():
    if my[k] > my[mk]:
      mk = k

  return mk

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
