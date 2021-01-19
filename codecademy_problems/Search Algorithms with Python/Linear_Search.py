def linear_search(search_list, target_value):
  for i in range(len(search_list)):
    print(search_list[i])
    if target_value == search_list[i]:
      return i
  raise ValueError(f"{target_value} not in list")


values = [54, 22, 46, 99]
print(linear_search(values, 221))
