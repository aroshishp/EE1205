import matplotlib.pyplot as plt
import numpy as np
limit = 100

def V_R_t(w, R, C, t):    
    ans = 0
    for n in range(1, limit, 2):
        ans += ((n * w * R * C)/(np.sqrt(1 + ((n*w*R*C)**2)))) * ((4 * np.sin(n * np.pi / 2) * np.cos(n * np.pi)) / (n * np.pi)) * (np.cos((n * w * t) + np.arctan(1 / (n * w * R * C))))

    return ans

def V_C_t(w, R, C, t):    
    ans = 0
    for n in range(1, limit, 2):
        ans += ((1)/(np.sqrt(1 + ((n*w*R*C)**2)))) * ((4 * np.sin(n * np.pi / 2) * np.cos(n * np.pi)) / (n * np.pi)) * (np.cos((n * w * t) - np.arctan((n * w * R * C))))

    return ans

t = np.linspace(0, 0.002, 1000)
w = 2 * np.pi * 1000
T = 0.001

#Option A
R = 500
C = 0.1 * (10 ** (-6))

V_A_out = V_R_t(w, R, C, t)
plt.plot(t, V_A_out/2)
plt.xticks(np.arange(0, 2.01*T, 0.0005), np.arange(0, 2.01*T, 0.0005) * 1e4)
plt.xlabel('t ($10^{-4}$ sec)')
plt.ylabel('$V_{out}$ (V)')
plt.grid(True)
plt.show()

#Option B
R = 5000
C = (10 ** (-6))

V_B_out = V_R_t(w, R, C, t)
plt.plot(t, V_B_out/2)
plt.xticks(np.arange(0, 2.01*T, 0.0005), np.arange(0, 2.01*T, 0.0005) * 1e4)
plt.xlabel('t ($10^{-4}$ sec)')
plt.ylabel('$V_{out}$ (V)')
plt.grid(True)
plt.show()

#Option C
limit = 50
R = 500
C = (10 ** (-7))

V_C_out = V_C_t(w, R, C, t)
plt.plot(t, V_C_out/2)
plt.xticks(np.arange(0, 2.01*T, 0.0005), np.arange(0, 2.01*T, 0.0005) * 1e4)
plt.xlabel('t ($10^{-4}$ sec)')
plt.ylabel('$V_{out}$ (V)')
plt.grid(True)
plt.show()

#Option D
R = 5000
C = (10 ** (-6))

V_D_out = V_C_t(w, R, C, t)
plt.plot(t, V_D_out/2)
plt.xticks(np.arange(0, 2.01*T, 0.0005), np.arange(0, 2.01*T, 0.0005) * 1e4)
plt.xlabel('t ($10^{-4}$ sec)')
plt.ylabel('$V_{out}$ (V)')
plt.grid(True)
plt.show()