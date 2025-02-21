import numpy as np
import matplotlib.pyplot as plt

# Tham số
bit_rate = 1  # Tốc độ bit (bps)
fs = 100  # Tần số lấy mẫu (Hz)
fc = 10   # Tần số sóng mang (Hz)
bits = [1, 0, 1, 1, 0]  # Dữ liệu đầu vào

# Tạo tín hiệu
T = 1 / bit_rate  # Thời gian của mỗi bit
t = np.arange(0, T * len(bits), 1 / fs)  # Trục thời gian

# Tạo tín hiệu bit
bit_signal = np.repeat(bits, fs // bit_rate)

# Tạo sóng mang
carrier = np.sin(2 * np.pi * fc * t)

# Điều chế ASK
ask_signal = bit_signal * carrier

# Vẽ đồ thị
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.step(t, bit_signal, where='post')
plt.ylim(-0.2, 1.2)
plt.title('Chuỗi Bit')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')

plt.subplot(3, 1, 2)
plt.plot(t, carrier, 'r')
plt.title('Sóng Mang')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')

plt.subplot(3, 1, 3)
plt.plot(t, ask_signal, 'g')
plt.title('Tín Hiệu ASK')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')

plt.tight_layout()
plt.show()
