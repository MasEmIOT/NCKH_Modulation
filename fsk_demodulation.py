import numpy as np
import matplotlib.pyplot as plt

# Tham số
bit_rate = 1  
fs = 100  
f0 = 5    
f1 = 10   
num_bits = 10  # Số bit ngẫu nhiên

# Sinh chuỗi bit ngẫu nhiên
bits = np.random.randint(0, 2, num_bits).tolist()

# Tạo tín hiệu
T = 1 / bit_rate  
t = np.arange(0, T * len(bits), 1 / fs)  
fsk_signal = np.zeros_like(t)
for i, bit in enumerate(bits):
    f = f1 if bit else f0
    fsk_signal[i * fs // bit_rate : (i + 1) * fs // bit_rate] = np.sin(2 * np.pi * f * t[i * fs // bit_rate : (i + 1) * fs // bit_rate])

# Giải điều chế FSK
demod_f0 = np.sin(2 * np.pi * f0 * t) * fsk_signal  
demod_f1 = np.sin(2 * np.pi * f1 * t) * fsk_signal  
energy_f0 = np.array([np.mean(demod_f0[i * fs // bit_rate: (i + 1) * fs // bit_rate]) for i in range(len(bits))])
energy_f1 = np.array([np.mean(demod_f1[i * fs // bit_rate: (i + 1) * fs // bit_rate]) for i in range(len(bits))])
received_bits = (energy_f1 > energy_f0).astype(int)  

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
plt.plot(t, np.sin(2 * np.pi * f1 * t), 'r')
plt.title('Sóng Mang FSK')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')

plt.subplot(3, 1, 3)
plt.plot(t, fsk_signal, 'g')
plt.title('Tín Hiệu FSK')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')

plt.tight_layout()
plt.show()
