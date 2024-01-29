import matplotlib.pyplot as plt 
import numpy as np 

#Read data from nx_values.dat
data = np.loadtxt('nx_values.dat')

#assign data to lists
n_values, x_values = data[:, 0], data[:, 1]

#Plot stem graph
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('x_plot.png')
#plt.show()
