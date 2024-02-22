import matplotlib.pyplot as plt
import numpy as np 

def square_wave(t, T):
    return (2 * (2 * np.floor((t - T/4)/T) - np.floor(2 * (t - T/4) / T)) + 1) * ( t > T/4)

def H_f_R(R, C, freq):
    return np.where(freq != 0, R / (R + 1 / (1j * 2 * np.pi * freq * C)), 0)

def H_f_C(R, C, freq):
    return np.where(freq != 0, (1 / 1j * 2 * np.pi * freq * C) / (R + 1 / (1j * 2 * np.pi * freq * C)), 0)

def fourier_ser(n, t, T):
    ans = 0
    for i in range(1, n+2):
        ans += ((4 * np.sin(i * np.pi / 2) * np.cos(i * np.pi)) / (i * np.pi)) * np.cos(2 * np.pi * i * t / T) * (t > T/4)
    return (ans)

T = 0.001
t = np.linspace(0, 2 * T, 10000)

V_in_1 = fourier_ser(1, t, T)
V_in_2 = fourier_ser(2, t, T)
V_in_3 = fourier_ser(3, t, T)
V_in_4 = fourier_ser(4, t, T)
V_in_5 = fourier_ser(5, t, T)
V_in_t = square_wave(t, T)

plt.plot(t, V_in_1, color = 'green', label = 'n=1')
# plt.plot(t, V_in_2)
plt.plot(t, V_in_3, color = 'red', label = 'n=3')
# plt.plot(t, V_in_4)
plt.plot(t, V_in_5, color = 'yellow', label = 'n=5')
plt.plot(t, V_in_t, color = 'blue')
plt.xticks(np.arange(0, 2.01*T, 0.0005), np.arange(0, 2.01*T, 0.0005) * 1e4)
plt.xlabel('t ($10^{-4}$ sec)')
plt.ylabel('$V_{in}$ (V)')
plt.grid(True)
# plt.savefig('square.png')
plt.legend(['n=1', 'n=3', 'n=5'])
plt.show()
plt.clf()

V_in_f = np.fft.fft(V_in_t)
freq = np.fft.fftfreq(len(V_in_t), t[1] - t[0])

plt.plot(freq, V_in_f)
plt.xlabel('Frequency ($f$)')
plt.ylabel('Fourier Transform of $V_{in}$')
plt.grid(True)
# plt.savefig('square_fourier.png')
# plt.show()
plt.clf()

#Option A
R = 500
C = 0.1 * 10 ** (-6)

V_out_f_R_A = H_f_R(R, C, freq) * V_in_f
V_out_t_A = np.where(t > T/4, np.fft.ifft(V_out_f_R_A), 0)
V_out_t_A_normalized = V_out_t_A.real / np.max(np.abs(V_out_t_A.real))

plt.plot(t, V_out_t_A_normalized)
plt.xticks(np.arange(0, 2.01*T, 0.0005), np.arange(0, 2.01*T, 0.0005) * 1e4)
plt.xlim(0.5 * T, 2 * T)
plt.xlabel('t ($10^{-4}$ sec)')
plt.ylabel('$V_{out}$ (V)')
plt.grid(True)
# plt.savefig('opt_a_res.png')
# plt.show()
plt.clf()

plt.plot(freq, V_out_f_R_A)
plt.xlabel('Frequency (f)')
plt.ylabel('FT of $V_{out}(t)$')
plt.grid(True)
# plt.show()
# plt.savefig('opt_a_ft.png')
plt.clf()

#Option B
R = 5000
C = 10**(-6)

V_out_f_R_B = H_f_R(R, C, freq) * V_in_f
V_out_t_B = np.fft.ifft(V_out_f_R_B)
V_out_t_B_normalized = V_out_t_B.real / np.max(np.abs(V_out_t_B.real))

plt.plot(t, V_out_t_B_normalized)
plt.title('Response of Option (b)')
plt.xticks(np.arange(0, 2.01*T, 0.0005), np.arange(0, 2.01*T, 0.0005) * 1e4)
plt.xlabel('t ($10^{-4}$ sec)')
plt.ylabel('$V_{out}$ (V)')
plt.grid(True)
# plt.show()
# plt.savefig('opt_b_res.png')
plt.clf()

plt.plot(freq, V_out_f_R_B)
plt.xlabel('Frequency (f)')
plt.ylabel('FT of $V_{out}(t)$')
plt.grid(True)
# plt.show()
# plt.savefig('opt_b_ft.png')
plt.clf()

#Option C
R = 500
C = 0.1 * 10 ** (-6)

V_out_f_C_C = H_f_C(R, C, freq) * V_in_f
V_out_t_C = np.fft.ifft(V_out_f_C_C)
V_out_t_C_normalized = V_out_t_C.real / np.max(np.abs(V_out_t_C.real))

plt.plot(t, V_out_t_C_normalized)
plt.xticks(np.arange(0, 2.01*T, 0.0005), np.arange(0, 2.01*T, 0.0005) * 1e4)
plt.xlabel('t ($10^{-4}$ sec)')
plt.ylabel('$V_{out}$ (V)')
plt.grid(True)
# plt.show()
# plt.savefig('opt_c_res.png')
plt.clf()

plt.plot(freq, V_out_f_C_C)
plt.xlabel('Frequency (f)')
plt.ylabel('FT of $V_{out}(t)$')
plt.grid(True)
# plt.show()
# plt.savefig('opt_c_ft.png')
plt.clf()

#Option D
R = 5000
C = 10**(-6)

V_out_f_C_D = H_f_C(R, C, freq) * V_in_f
V_out_t_D = np.fft.ifft(V_out_f_C_D)
V_out_t_D_normalized = V_out_t_D.real / np.max(np.abs(V_out_t_D.real))

plt.plot(t, V_out_t_D_normalized)
plt.xticks(np.arange(0, 2.01*T, 0.0005), np.arange(0, 2.01*T, 0.0005) * 1e4)
plt.xlabel('t ($10^{-4}$ sec)')
plt.ylabel('$V_{out}$ (V)')
plt.grid(True)
# plt.show()
# plt.savefig('opt_d_res.png')
plt.clf()

plt.plot(freq, V_out_f_C_D)
plt.xlabel('Frequency (f)')
plt.ylabel('FT of $V_{out}(t)$')
plt.grid(True)
# plt.show()
# plt.savefig('opt_d_ft.png')
plt.clf()


