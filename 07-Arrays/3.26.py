import matplotlib.pyplot as plt
import math
x = []
y = []
#  y = sin(x)
# create x values
for n in range(0,360):
    x = x + [n]

# create y values
for n in x:
    y.append(math.sin(n))

# print chart
plt.plot(x, y)
plt.show()