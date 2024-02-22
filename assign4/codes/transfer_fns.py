import matplotlib.pyplot as plt
import numpy as np

def H_Res(w, R, C):
    return (1j * w * R * C)/(1 + (1j * w * R * C))

def H_Cap(w, R, C):
    return 1 / (1 + (1j * w * R * C))


#Option A
R = 500
C = 0.1 * 10 ** (-6)
w = np.linspace(0, 300000, 1000000)

H_A = H_Res(w, R, C)
plt.plot(w, np.abs(H_A))
plt.xlabel('$\omega$')
plt.ylabel('|$H_R(j\omega)$|')
# plt.title("H_A")
plt.grid(True)
plt.savefig('opt_a_hf.png')
plt.show()
plt.clf()

#Option B
R = 5000
C = 10 ** (-6)
w = np.linspace(0, 20000, 1000000)

H_B = H_Res(w, R, C)
plt.plot(w, np.abs(H_B))
plt.xlabel('$\omega$')
plt.ylabel('|$H_R(j\omega)$|')
# plt.title("H_B")
plt.grid(True)
plt.savefig('opt_b_hf.png')
plt.show()
plt.clf()

#Option C
R = 500
C = 0.1 * 10 ** (-6)
w = np.linspace(0, 300000, 1000000)

H_C = H_Cap(w, R, C)
plt.plot(w, np.abs(H_C))
plt.xlabel('$\omega$')
plt.ylabel('|$H_C(j\omega)$|')
# plt.title("H_C")
plt.grid(True)
plt.savefig('opt_c_hf.png')
plt.show()
plt.clf()

#Option D
R = 5000
C = 10 ** (-6)
w = np.linspace(0, 60000, 1000000)

H_D = H_Cap(w, R, C)
plt.plot(w, np.abs(H_D))
plt.xlabel('$\omega$')
plt.ylabel('|$H_C(j\omega)$|')
# plt.title("H_D")
plt.grid(True)
plt.savefig('opt_d_hf.png')
plt.show()
plt.clf()