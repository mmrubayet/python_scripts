# Uses of exception
# Section 5.1.6.4

def readint(prompt, min, max):
    try:
        prompt = int(prompt)
        assert -10 <= prompt <= 10
    except ValueError:
        print("Error: wrong input")
        return readint(input("Enter a number from -10 to 10: "), -10, 10)

    except AssertionError:
        print("Error: the value is not within permitted range (-10..10)")
        return readint(input("Enter a number from -10 to 10: "), -10, 10)
    return prompt


v = readint(input("Enter a number from -10 to 10: "), -10, 10)


print("The number is:", v)
