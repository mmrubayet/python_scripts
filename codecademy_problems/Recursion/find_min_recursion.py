def find_min(list, min = None):
  if len(list) == 0:
    return min
  else:
    if min == None or list[0] < min:
      min = list[0]
  return find_min(list[1:], min)

# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)
