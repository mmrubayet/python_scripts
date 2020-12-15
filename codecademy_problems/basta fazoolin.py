
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}


class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_item):
    total = 0
    for item in purchased_item:
      total += self.items[item]
    return total


brunch = Menu("Brunch", brunch_items, 11, 16)
early_bird = Menu("Early Bird", early_bird_items, 15, 18)
dinner = Menu("Dinner", dinner_items, 17, 23)
kids = Menu("Kids", kids_items, 11, 21)

# print(brunch)
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
menus = [brunch, early_bird, dinner, kids]

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def getName(self):
    return self.__class__.__name__

  def __repr__(self):
    return f"Address of {self.getName()}: {self.address}"

  def available_menus(self, time):
    am = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        am.append(menu.name)
    return am


flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# print(flagship_store)
# print(new_installment)
# print(flagship_store.available_menus(17))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


franchises = [flagship_store, new_installment]

Business("Basta Fazoolin' with my Heart", franchises)


arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a’ Arepa", arepas_menu, 10, 22)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)


Business("Take a' Arepa", arepas_place)
