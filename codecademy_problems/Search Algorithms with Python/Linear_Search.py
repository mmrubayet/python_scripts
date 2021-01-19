number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33

def linear_search(search_list, target_value):
  for i in range(len(search_list)):
    print(search_list[i])
    if target_value == search_list[i]:
      return i
  raise ValueError(f"{target_value} not in list")


try:
  result = linear_search(number_list, 100 )
  print(result)

except ValueError as error_message:
  print("{0}".format(error_message))
