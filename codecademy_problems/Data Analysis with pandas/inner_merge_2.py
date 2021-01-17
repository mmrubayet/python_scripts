# import codecademylib
import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

men_women = pd.read_csv('men_women_sales.csv')
print(men_women)

all_data = sales.merge(targets).merge(men_women)
print(all_data)

results = all_data[(all_data['revenue'] >= all_data['target']) & (all_data['women'] > all_data['men'])].reset_index(drop=True)

print(results)
