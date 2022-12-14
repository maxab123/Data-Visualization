import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('Data_fill.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 572872

plt.fill_between(ages, py_salaries, alpha=0.25,
    where=(py_salaries > dev_salaries) , interpolate=True, y2=dev_salaries ,label = "Above avg")

plt.fill_between(ages, py_salaries, alpha=0.25,
    where=(py_salaries < dev_salaries) , color="red", interpolate=True, y2=dev_salaries ,label = "Above avg")
plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()