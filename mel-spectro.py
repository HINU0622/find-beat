import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import glob

# 1. Load audio file

for wav_file in glob.glob('.\\that_removed.wav'):
  print(wav_file)
  audio_file = wav_file
  y, sr = librosa.load(audio_file)

  # 2. Extract Mel Spectrogram
  mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)

  # 3. Convert to log scale
  log_mel_spec = librosa.amplitude_to_db(mel_spec, ref=np.max)

  # 4. Save Mel Spectrogram as image
  fig = plt.figure(figsize=(1, 1), dpi=128)
  ax = fig.add_subplot(111)
  ax.axis('off')
  ax.imshow(log_mel_spec, cmap='magma', aspect='auto', origin='lower')
  plt.tight_layout(pad=0)
  plt.subplots_adjust(wspace=0, hspace=0, top=1, bottom=0, left=0, right=1)
  plt.savefig('./' + wav_file.split('\\')[1].split('.')[0] + '.png', bbox_inches='tight', pad_inches=0, transparent=True)