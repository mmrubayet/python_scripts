# LAB: Find a word
# 5.1.11.10
import re
s1 = input("Enter String 1: ").lower()
s2 = input("Enter String 2: ").lower()

print((re.search('.*'.join(s1), s2) and "YES") or "NO")
