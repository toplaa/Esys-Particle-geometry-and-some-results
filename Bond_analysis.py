import matplotlib.pyplot as plt
import numpy as np

DataIn = np.loadtxt('nbonds.dat')

#usecols uses the first two columns
y = np.loadtxt('nbonds.dat', unpack=True)
x = range(0,len(y))

y_init= y[0]

y2 = ((y_init-y)/y_init)*100

#pick portion of graph to plot
#start_point = 300000
#end_point   = 600000

#plt.scatter(x[start_point:end_point],y[start_point:end_point], label='loaded file')

#plt.plot(x,y, label='Bonds')
plt.plot(x,y2)

plt.xlim([0, 400000])
#plt.title('Bond graph')
plt.xlabel('Timestep number')
plt.ylabel('% of broken bonds')
plt.legend()
plt.grid()
plt.show()
