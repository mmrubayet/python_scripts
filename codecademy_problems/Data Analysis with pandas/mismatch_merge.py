import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

print(products)
print(orders)

merged_df = pd.merge(orders, products)

print(merged_df)
