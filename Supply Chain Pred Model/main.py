import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, LSTM
from keras.optimizers import Adam
from keras.metrics import sparse_categorical_crossentropy
import matplotlib.pyplot as plt

import numpy as np

#NOT USING PICKLE DATA; DIRECT IMPORTS
from data_preprocess import Msia_cal_per_day as a1
from data_preprocess import Msia_chicken_consumption_yearly as a2
from data_preprocess import Msia_exchange_rates as a3
from data_preprocess import Msia_inflation_data as a4
from data_preprocess import Msia_labour_data as a5
from data_preprocess import Msia_political_instability as a6

a1 = a1 / 3000
a2 = a2 / 100000000
a4 = a4 / 100000000
a5 = a5 / 100000000


y = np.column_stack((a1, a2, a3, a4, a5, a6))
#y = tf.keras.utils.to_categorical(y, num_classes=6) #one hot 
#shape: 57, 6

#year series
x = []
for i in range(1961, 2018):
    x.append(i)

x = np.array(x)
x = x.reshape(-1, 1, 1)
x = x / 2000

Model = Sequential()

Model.add(LSTM(32, input_shape = (1, 1), activation='relu', return_sequences=True))
Model.add(Dropout(0.1))

Model.add(LSTM(128, activation='relu'))
Model.add(Dropout(0.1))

Model.add(Dense(32, activation="relu"))
Model.add(Dropout(0.1))

Model.add(Dense(6, activation="linear"))


optim = Adam(lr=1e-3, decay=1e-5)
Model.compile(optimizer=optim, loss="mean_squared_error", metrics=["mean_squared_error"])
Model.fit(x, y, batch_size=10, epochs=30)


prediction = Model.predict(np.array([2023 / 2000]).reshape(1, 1))

print(prediction)
