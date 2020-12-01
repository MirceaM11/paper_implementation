#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import matplotlib.pyplot as plt
import numpy as np


root_list = np.array(["P1WINS",  "P2WINS",  "EQUALITIES"])

y1 = np.array([73.27, 6.73, 20])
y2 = np.array([50, 50, 0])
y3 = np.array([45, 30, 25])
y4 = np.array([15, 45, 40])

x = np.arange(len(root_list))
width = 0.35

fig = plt.subplots(ncols=1, nrows=3)
plt.title('Results for P1 as pivot')
plt.xlabel('Results')
plt.ylabel('P1:Cooperator')
i = 1
while i <= 3:
    axes = plt.subplot(1, 3, i)
    print(type(axes))
    axes.bar(x, y1, width=width, label="P2:{}".format(i))
    axes.set_xticks(x)
    axes.set_xticklabels(['P1W', 'P2W', 'EQ'])
    i+=1

plt.show()
plt.close()