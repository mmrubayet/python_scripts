def factorial(n):
  if n == 1 or n == 0:
    return n
  return n * factorial(n-1)

# print(factorial(12))
print(factorial(998))
# print(factorial(999))
