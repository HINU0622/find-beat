import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten, GlobalAveragePooling2D
import numpy as np
import pandas as pd
import glob

paths = glob.glob('./dt5/spec/*.png')

train_x = np.array([plt.imread(paths[i]) for i in range(len(paths))])
train_y = np.array([paths[i].split('\\')[1] for i in range(len(paths))])

beat_count = len(train_y)

with open('./list.txt', 'w', encoding='utf-8') as f:
    for i in range(beat_count):
        f.writelines('{} : {}\n'.format(i, train_y[i]))

train_y = pd.get_dummies(train_y, columns=['name'])
columns = train_y.columns

print(train_x.shape, train_y.shape)



drop_out = 0.5

model = Sequential()

model.add(Conv2D(input_shape=(128, 128, 4), filters=16, kernel_size=3, activation='swish'))
model.add(Dropout(drop_out))

model.add(Conv2D(kernel_size=3, filters=32, activation='swish'))
model.add(Dropout(drop_out))

model.add(Conv2D(kernel_size=3, filters=64, activation='swish'))
model.add(Dropout(drop_out))

model.add(Conv2D(kernel_size=3, filters=128, activation='swish'))
model.add(Dropout(drop_out))

model.add(Flatten())

model.add(Dense(units=89, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# model.load_weights('weights')

model.fit(train_x, train_y, epochs=30, batch_size=128)

model.save_weights('weights')