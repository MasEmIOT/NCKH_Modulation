import numpy as np
import matplotlib.pyplot as plt

# Tham số
bit_rate = 1   # Tốc độ bit (bps)
fs = 100       # Tần số lấy mẫu (Hz)
f0 = 5         # Tần số sóng mang cho bit 0 (Hz)
f1 = 10        # Tần số sóng mang cho bit 1 (Hz)
bits = [1, 0, 1, 1, 0]  # Chuỗi bit

# Tạo trục thời gian
T = 1 / bit_rate  # Thời gian của mỗi bit
t = np.arange(0, T * len(bits), 1 / fs)

# Tạo tín hiệu FSK
fsk_signal = np.zeros_like(t)
for i, bit in enumerate(bits):
    f = f1 if bit else f0  # Chọn tần số theo bit
    fsk_signal[i * fs // bit_rate : (i + 1) * fs // bit_rate] = np.sin(2 * np.pi * f * t[i * fs // bit_rate : (i + 1) * fs // bit_rate])

# Vẽ đồ thị
plt.figure(figsize=(10, 4))
plt.plot(t, fsk_signal)
plt.title("Tín hiệu FSK")
plt.xlabel("Thời gian (s)")
plt.ylabel("Biên độ")
plt.grid()
plt.show()
