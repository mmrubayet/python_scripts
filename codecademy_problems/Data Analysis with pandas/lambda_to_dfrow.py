import codecademylib
import pandas as pd

df = pd.read_csv('employees.csv')

total_earned = lambda x : (x.hourly_wage * 40) + \
((x.hourly_wage * 1.5) * (x.hours_worked - 40))  \
if x.hours_worked > 40 else x.hourly_wage * x.hours_worked


df['total_earned'] = df.apply(total_earned, axis=1)

print(df)
