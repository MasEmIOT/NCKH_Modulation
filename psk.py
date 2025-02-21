import numpy as np
import matplotlib.pyplot as plt

# Tham số
bit_rate = 1   # Tốc độ bit (bps)
fs = 100       # Tần số lấy mẫu (Hz)
fc = 10        # Tần số sóng mang (Hz)
bits = [1, 0, 1, 1, 0, 1, 0, 0]  # Chuỗi bit (phải có số chẵn)

# Định dạng dữ liệu thành cặp (I, Q)
bit_pairs = np.array(bits).reshape(-1, 2)  # Nhóm 2 bit một

# Tạo trục thời gian
T = 1 / bit_rate
t = np.arange(0, T * len(bit_pairs), 1 / fs)

# Tạo tín hiệu sóng mang
carrier_I = np.cos(2 * np.pi * fc * t)
carrier_Q = np.sin(2 * np.pi * fc * t)

# Mã hóa tín hiệu QSK
QSK_signal = np.zeros_like(t)
for i, (b1, b2) in enumerate(bit_pairs):
    I = 1 if b1 else -1
    Q = 1 if b2 else -1
    start = i * fs // bit_rate
    end = (i + 1) * fs // bit_rate
    QSK_signal[start:end] = I * carrier_I[start:end] + Q * carrier_Q[start:end]

# Vẽ đồ thị
plt.figure(figsize=(10, 4))
plt.plot(t, QSK_signal)
plt.title("Tín hiệu QSK")
plt.xlabel("Thời gian (s)")
plt.ylabel("Biên độ")
plt.grid()
plt.show()
