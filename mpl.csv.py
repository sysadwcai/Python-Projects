import csv
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

with open('DevSalary.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title("Most Popular Languages")
#plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()
plt.show()
