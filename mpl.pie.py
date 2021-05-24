from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

#slices = [120, 80, 30, 20]
#labels = ['Sixty', 'Fourty', 'Extra1', 'Extra2']

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]  # 0.1% distance away from radius
# colors = ['#008fd5', '#fc4f30', 'e5ae37', '#6d904f'] hex colors

plt.pie(slices, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%',
        startangle=90, wedgeprops={'edgecolor': 'black'})  # colors=colors

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
