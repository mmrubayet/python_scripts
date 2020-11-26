# seven_segment display
# Section 5.1.10.6
rep = [
    ['* * *', '*   *', '*   *', '*   *', '* * *'],
    ['    *', '    *', '    *', '    *', '    *'],
    ['* * *', '    *', '* * *', '*    ', '* * *'],
    ['* * *', '    *', '* * *', '    *', '* * *'],
    ['*   *', '*   *', '* * *', '    *', '    *'],
    ['* * *', '*    ', '* * *', '    *', '* * *'],
    ['* * *', '*    ', '* * *', '*   *', '* * *'],
    ['* * *', '    *', '    *', '    *', '    *'],
    ['* * *', '*   *', '* * *', '*   *', '* * *'],
    ['* * *', '*   *', '* * *', '    *', '* * *'],
    ['     ', '     ', '     ', '     ', '    *'],
]


def seven_segment(number):
    digits = [rep[int(digit)] for digit in list(number)]
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))

num = input("Enter a Number: ")

seven_segment(num)
