def is_palindrome(s):
  if len(s) < 2:
    return True
  if s[0] != s[-1]:
    return False
  return is_palindrome(s[1:-1])


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)
