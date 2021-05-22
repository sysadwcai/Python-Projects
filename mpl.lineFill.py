from numpy import put_along_axis
import pandas as pd
from matplotlib import colors, pyplot as plt

data = pd.read_csv('SalaryByAge.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

overall_median = 57287
plt.plot(ages, dev_salaries, colors='#444444',
         linestyle='--', labels='All Devs')
plt.plot(ages, py_salaries, labels='Python')

'''plt.fill_between(ages, py_salaries, overall_median, where=(
    py_salaries > overall_median), interpolate=True, alpha=0.25)
plt.fill_between(ages, py_salaries, overall_median, where=(
    py_salaries <= overall_median), interpolate=True, color='red', alpha=0.25)
'''
plt.fill_between(age, py_salaries, dev_salaries, where=(
    py_salaries > dev_salaries), interpolate=True, alpha=0.25, labels='Above Avg')
plt.fill_between(ages, py_salaries, dev_salaries, where=(
    py_salaries <= dev_salaries), interpolate=True, color='red', alpha=0.25, label='Below Avg')

plt.legend()
plt.title("Median Salary (USD) by age")
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD')
plt.show()
