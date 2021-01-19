def multiplication(a, b):
  if a == 0 or b == 0:
    return 0
  return a + multiplication(a, b-1 )


# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)
