import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.optimizers import Adam
from keras.metrics import sparse_categorical_crossentropy

import numpy as np

#NOT USING PICKLE DATA; DIRECT IMPORTS
from data_preprocess import Msia_cal_per_day as a1
from data_preprocess import Msia_chicken_consumption_yearly as a2
from data_preprocess import Msia_exchange_rates as a3
from data_preprocess import Msia_inflation_data as a4
from data_preprocess import Msia_labour_data as a5
from data_preprocess import Msia_political_instability as a6


y = np.column_stack((a1, a2, a3, a4, a5, a6))
#shape: 57, 6

#year series
x = []
for i in range(1961, 2018):
    x.append(i)

x = np.array(x)



Model = Sequential()

Model.add(Dense(32, activation='relu', input_dim=1))
Model.add(Dense(6, activation='relu'))
#Model.add(Dense(1, activation='sigmoid'))

Model.compile(optimizer="Adam", loss="binary_crossentropy", metrics=["accuracy"])

Model.fit(x, y, batch_size=10, epochs=30)


Model.predict([2020])
