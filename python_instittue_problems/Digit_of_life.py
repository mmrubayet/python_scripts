# Digit of Life
# 5.1.11.9

d = str(input()).replace(' ','')

while True:
    sum = 0
    for i in d:
        sum += int(i)
    d = str(sum)
    if len(d) < 2:
        break
    
print(d)
