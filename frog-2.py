import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import math
import random

count = 0
hops = 0
average = 0
remaining = 0
results = []
plot = []
#pad counts to test for
values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]
for i in values:
    remaining = i
    #run each value 5000 times
    while count <= 5000:
        if remaining > 0:
            remaining -= random.randint(1,remaining)
            hops +=1
        if remaining == 0:
            results.append(hops)
            average = sum(results) / len(results)
            count += 1
            hops = 0
            remaining = i
    results = []
    
    #print("values = ", i, "  count =", count-1, "  average =", average)
    #print("{:.2f}".format(average))
    plot.append("{:.2f}".format(average))
    count = 0
    print("Pad Count: ", i, "\tAverage: ", "{:.2f}".format(average))

plt.plot(values,plot)
plt.ylim([0, round(float(max(plot)))+1])
plt.show()
plt.savefig('test.png')

