tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

def linear_search(search_list, target_value):
  matches = []
  for i in range(len(search_list)):
    if search_list[i] == target_value:
      matches.append(i)
  if matches:
    return matches
  raise ValueError(f"{target_value} not in list")

tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)
