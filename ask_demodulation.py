import numpy as np
import matplotlib.pyplot as plt

# Tham số
bit_rate = 1  
fs = 100  
fc = 10   
num_bits = 10  # Số bit ngẫu nhiên

# Sinh chuỗi bit ngẫu nhiên
bits = np.random.randint(0, 2, num_bits).tolist()

# Tạo tín hiệu
T = 1 / bit_rate  
t = np.arange(0, T * len(bits), 1 / fs)  
bit_signal = np.repeat(bits, fs // bit_rate)  
carrier = np.sin(2 * np.pi * fc * t)  

# Điều chế ASK
ask_signal = bit_signal * carrier  

# Giải điều chế ASK
ask_demod = ask_signal * carrier  
ask_integrated = np.array([np.mean(ask_demod[i * fs // bit_rate: (i + 1) * fs // bit_rate]) for i in range(len(bits))])
received_bits = (ask_integrated > 0.2).astype(int)  

print("Chuỗi bit gốc:   ", bits)
print("Chuỗi bit nhận được:", received_bits.tolist())

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
