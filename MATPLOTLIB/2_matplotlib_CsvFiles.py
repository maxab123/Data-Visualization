import csv
import pandas as pd
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

#OPENING A CSV FILE USING THE CSV IMPORT
# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]
language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
print(languages)
print(popularity)
languages.reverse()
popularity.reverse()
plt.barh( languages, popularity)#takes the Y values first
plt.title("Most Popular Languages")
# plt.ylabel("Programming languages")
plt.xlabel("Percentage of People who use")
plt.show()





































