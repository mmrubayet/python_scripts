from swap import *

def bubble_sort(arr):
  for el in arr:
    for index in range(len(arr)-1):
      if arr[index] > arr[index + 1]:
        swap(arr, index, index + 1)


##### test statements
nums = [5, 2, 9, 1, 5, 6]
print("Pre-Sort: {0}".format(nums))
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))
