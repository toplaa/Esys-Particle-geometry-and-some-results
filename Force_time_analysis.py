#from __future__import division
import matplotlib.pyplot as plt
import numpy as np

DataIn = np.loadtxt('Steel_rod_Force.dat')

#usecols uses the first two columns
x, y = np.loadtxt('Steel_rod_Force.dat', unpack=True, usecols=[0,1])

#moving average
def movingaverage(interval, window_size):
	window = np.ones(int(window_size))/float(window_size)
	return np.convolve (interval, window, 'same')

x2 = range(0,len(x))

#Convert to (ms)
x3 =[]
for i in x2:
	x3.append(i*1e-06)


#plt.scatter(x[start_point:end_point],y[start_point:end_point], label='loaded file')
plt.plot(x3,y, label='Force-time history')

y_av = movingaverage(y, 6000)

#peak force
y_max = np.max(y_av)
y_sum = np.sum(y_av[:y_av.argmax()+1])

text_file = open("Force calculations.txt", "a")
text_file.write("peak force is %s\n" % y_max)
text_file.write("sum of forces to the peak point is %s" % y_sum)
text_file.close()


plt.plot (x3, y_av, label='Filtered Force-time history', color= 'r')



plt.xlim([0, 0.4])
#plt.title('Breakage graph')
plt.xlabel('Time (ms)')
plt.ylabel('Force (N)')
plt.legend()
plt.grid()
plt.show()

