import scipy.io.wavfile as wavfile
from scipy import signal
import matplotlib.pyplot as plt

# wav 파일 읽어오기
sample_rate, samples = wavfile.read('Return_original.wav')

# 스펙트로그램 계산
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

# 스펙트로그램 이미지 생성
plt.imshow(spectrogram, aspect='auto', origin='lower', cmap='jet')

# 이미지 저장
plt.savefig('spectrogram.png')