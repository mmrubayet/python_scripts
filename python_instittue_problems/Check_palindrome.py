# Check_palindrome
# 5.1.11.7

s = input("Enter a string: ")

s = s.replace(' ','')
s = s.lower()

if s == s[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome ")
