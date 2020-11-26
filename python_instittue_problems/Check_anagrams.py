# Check_anagrams
# 5.1.11.8

s = input("Enter a string: ").lower()
a = input("Enter a string: ").lower()


if sorted(s) == sorted(a):
    print("Anagrams")
else:
    print("Not anagrams")
