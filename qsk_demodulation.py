import numpy as np
import matplotlib.pyplot as plt

# Tham số
bit_rate = 1  
fs = 100  
fc = 10  
num_bits = 8  # Số bit ngẫu nhiên (phải là số chẵn)

# Sinh chuỗi bit ngẫu nhiên
bits = np.random.randint(0, 2, num_bits).tolist()

# Chia bit thành cặp (I, Q)
bit_pairs = np.array(bits).reshape(-1, 2)  

# Tạo tín hiệu
T = 1 / bit_rate  
t = np.arange(0, T * len(bit_pairs), 1 / fs)  
carrier_I = np.cos(2 * np.pi * fc * t)
carrier_Q = np.sin(2 * np.pi * fc * t)

# Điều chế QSK
QSK_signal = np.zeros_like(t)
for i, (b1, b2) in enumerate(bit_pairs):
    I = 1 if b1 else -1
    Q = 1 if b2 else -1
    start = i * fs // bit_rate
    end = (i + 1) * fs // bit_rate
    QSK_signal[start:end] = I * carrier_I[start:end] + Q * carrier_Q[start:end]

# Giải điều chế QSK
demod_I = QSK_signal * carrier_I
demod_Q = QSK_signal * carrier_Q
I_values = np.array([np.mean(demod_I[i * fs // bit_rate: (i + 1) * fs // bit_rate]) for i in range(len(bit_pairs))])
Q_values = np.array([np.mean(demod_Q[i * fs // bit_rate: (i + 1) * fs // bit_rate]) for i in range(len(bit_pairs))])
received_bits_I = (I_values > 0).astype(int)
received_bits_Q = (Q_values > 0).astype(int)
received_bits = np.column_stack((received_bits_I, received_bits_Q)).flatten()

print("Chuỗi bit gốc:   ", bits)
print("Chuỗi bit nhận được:", received_bits.tolist())

# Vẽ đồ thị
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.step(t, np.repeat(bits, fs // bit_rate), where='post')
plt.ylim(-0.2, 1.2)
plt.title('Chuỗi Bit')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')

plt.subplot(3, 1, 2)
plt.plot(t, carrier_I, 'r')
plt.title('Sóng Mang QSK (Cosine)')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')

plt.subplot(3, 1, 3)
plt.plot(t, QSK_signal, 'g')
plt.title('Tín Hiệu QSK')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')

plt.tight_layout()
plt.show()
