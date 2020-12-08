'''
Sal's Shipping

Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping
_______________

Weight of Package                       	 Price per Pound 	Flat Charge
2 lb or less 	                              $1.50 	         $20.00
Over 2 lb but less than or equal to 6 lb 	  $3.00              $20.00
Over 6 lb but less than or equal to 10 lb 	  $4.00              $20.00
Over 10 lb 	                                  $4.75 	         $20.00


Drone Shipping
______________

Weight of Package 	                         Price per Pound     Flat Charge
2 lb or less 	                              $4.50               $0.00
Over 2 lb but less than or equal to 6 lb 	  $9.00               $0.00
Over 6 lb but less than or equal to 10 lb 	  $12.00 	          $0.00
Over 10 lb 	                                  $14.25 	          $0.00

Premium Ground Shipping
Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

'''
def shipping(weight):
  gs = g_ship(weight)
  ds = d_ship(weight)
  cheap = 0
  via = " "

  if ds < gs and ds < pgs:
    cheap = ds
    via = "drone"
  elif gs < ds and gs < pgs:
    cheap = gs
    via = "ground"
  else:
    cheap = pgs
    via = "premium ground shipping"

  print(f"You should ship using {via} shipping, it will cost ${cheap}")

def g_ship(weight):
  if weight <= 2:
    return weight*1.50 + 20
  elif 2 < weight <= 6:
    return weight*3.00 + 20
  elif 6 < weight <= 10:
    return weight*4.00 + 20
  elif weight > 10:
    return weight*4.75 + 20

def d_ship(weight):
  if weight <= 2:
    return weight*4.50
  elif 2 < weight <= 6:
    return weight*9.00
  elif 6 < weight <= 10:
    return weight*12.00
  elif weight > 10:
    return weight*14.25

pgs = 125.00

shipping(41.5)
