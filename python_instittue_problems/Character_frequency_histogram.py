# 6.1.9.15 LAB: Character frequency histogram 
from os import strerror

srcname = input("Source file name?: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)	
dstname = input("Destination file name?: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create destination file: ",
    strerror(e.errno))
    src.close()
    exit(e.errno)	


word=input("Enter a string: ")
 
dictionary={}
 
for letter in word:
    if letter in dictionary:
        dictionary[letter]=dictionary[letter]+1
    else:
        dictionary[letter]=1
 
print(dictionary)
