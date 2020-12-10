### Problem

'''
Substring Between

Write a function named substring_between_letters that takes a string named word,
a single character named start, and another character named end. This function
should return the substring between the first occurrence of start and end in
word. If start or end are not in word, the function should return word.

For example, substring_between_letters("apple", "p", "e") should return "pl".

'''
### Solution


# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  s = word.find(start)
  e = word.find(end)
  if s == -1 or e == -1:
    return word
  else:
    return word[s+1:e]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
