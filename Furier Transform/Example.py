import numpy as np
import matplotlib.pyplot as plt

def fft(signal):
    N = len(signal)
    if N <= 1:
        return signal
    even = fft(signal[0::2])
    odd = fft(signal[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(min(len(odd), len(even)))]
    return [even[k] + T[k] for k in range(len(T))] + [even[k] - T[k] for k in range(len(T))]

# Exemplo de uso
# Gere um sinal de exemplo (uma soma de senos)
fs = 1000  # Frequência de amostragem
t = np.arange(0, 1, 1/fs)  # Vetor de tempo de 0 a 1 segundo com passo 1/fs
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)  # Sinal com componentes de 50 Hz e 120 Hz

# Aplica a FFT ao sinal
transformada = fft(signal)

# Calcula as frequências correspondentes
frequencias = np.fft.fftfreq(len(signal), 1/fs)

# Plota o sinal e sua transformada
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Sinal de Exemplo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(frequencias[:len(transformada)], np.abs(transformada))
plt.title('Transformada de Fourier')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
