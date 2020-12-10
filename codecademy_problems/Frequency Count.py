### Problem:
'''
Write a function named frequency_dictionary that takes a list of
elements named words as a parameter. The function should return a
dictionary containing the frequency of each element in words.

'''

### Soltuion:


def frequency_dictionary(words):
  md = {}
  for word in words:
    md[word] = words.count(word)
  return md



# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
