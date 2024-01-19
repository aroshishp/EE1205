import matplotlib.pyplot as plt
import numpy as np

#x(n) = 0.75n + 2
def x(n):
    return (0.75 * n + 2) * (n >= 0)

    
n_values = np.arange(-6, 8, 1)
x_values = x(n_values)

plt.stem(n_values, x_values)
plt.title('Plot of x(n) = ($\dfrac{3}{4}n + 2)u(n)$')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid(True)
#plt.show()
plt.savefig('fig2.png')
