def sum_to_one(n):
  if n == 1:
    return n
  print(f"Recursing with input: {n}")
  return n + sum_to_one(n-1)

print(sum_to_one(7))
