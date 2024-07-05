import numpy as np
import sounddevice as sd
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Frekans tablosu
note_freqs = {
    'E2': 82.41,
    'A2': 110.00,
    'D3': 146.83,
    'G3': 196.00,
    'B3': 246.94,
    'E4': 329.63,
}

# Ses parametreleri
SAMPLE_RATE = 44100  # Örnekleme frekansı
DURATION = 1  # Kayıt süresi (saniye)

# En yakın notayı bulma fonksiyonu
def closest_note(freq):
    closest = min(note_freqs.keys(), key=lambda note: abs(note_freqs[note] - freq))
    return closest, note_freqs[closest]

# Frekans analizi fonksiyonu
def analyze_frequency(audio, sample_rate):
    N = len(audio)
    yf = fft(audio)
    xf = fftfreq(N, 1 / sample_rate)
    # Pozitif frekansları al
    xf = xf[:N // 2]
    yf = np.abs(yf[:N // 2])
    # En yüksek genlikli frekansı bul
    idx = np.argmax(yf)
    freq = xf[idx]
    return freq

# Gitar akort kontrolü
def tune_instrument():
    # 1 saniye boyunca ses kaydet
    print("Kaydediliyor...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float64')
    sd.wait()  # Kayıt tamamlanana kadar bekle
    print("Kayıt tamamlandı.")
    
    # Frekans analizi
    freq = analyze_frequency(audio[:, 0], SAMPLE_RATE)
    note, note_freq = closest_note(freq)
    print(f"Çalınan frekans: {freq:.2f} Hz, En yakın nota: {note} ({note_freq} Hz)")
    
    # Geri bildirim
    ax.clear()
    ax.plot(audio)
    ax.set_title(f"Çalınan Frekans: {freq:.2f} Hz, Nota: {note}")
    ax.set_xlabel("Zaman")
    ax.set_ylabel("Genlik")
    ax.grid()
    plt.draw()

# Anlık güncellemeleri görselleştirmek için matplotlib ayarları
plt.ion()
fig, ax = plt.subplots()

# Ses akışını başlat
def main():
    print("Gitarın akordunu kontrol etmek için bir tel çalın...")
    while True:
        tune_instrument()
        plt.pause(1)  # 1 saniye bekle

if __name__ == "__main__":
    main()
