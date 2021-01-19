def merge_sort(items):
  if len(items) <= 1:
    return items
  middle_index = len(items)//2
  left_split = items[:middle_index]
  right_split = items[middle_index:]
  return middle_index, left_split, right_split
