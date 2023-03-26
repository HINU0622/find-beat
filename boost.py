import wave, numpy, struct, glob

boost_size = 2 # 부스트 할 크기 (기본 2배)

for file in glob.glob('./that_removed.wav'):

  print(file)
  # Open
  w = wave.open(file, "rb")
  p = w.getparams()
  f = p[3] # number of frames
  s = w.readframes(f)
  w.close()

  # Edit
  s = numpy.fromstring(s, numpy.int16) * boost_size
  print(s)
  s = struct.pack('h'*len(s), *s)

  # Save
  w = wave.open(file, "wb")
  w.setparams(p)
  w.writeframes(s)
  w.close()