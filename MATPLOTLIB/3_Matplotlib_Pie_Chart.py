import matplotlib
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [ 60, 40, 30, 20]
labels = ["Sixty", "forty","Extra1", "Extra2"]
colors = ["#008fd5", "#fc4f30", "#e5ae37","#6d904f"]

labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
slices = [59219, 55466, 47544, 36443, 35917]
explode = [0, 0, 0, 0.1, 0] #for emphasizing on a particular item on the pie chart.

plt.pie(slices, labels=labels,wedgeprops={"edgecolor":"black"}, explode=explode, 
    shadow=True, startangle=90, autopct="%1.1f%%")

plt.title("my Awesome Pie Chart")
plt.tight_layout()
plt.show()


