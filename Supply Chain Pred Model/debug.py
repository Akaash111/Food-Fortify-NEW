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
from main import y

a1 = a1
a1_mean = (a1 * 57) / 57
a1_std = np.std(a1)
A1 = []
for ele in a1: 
    ele = (ele - a1_mean) / a1_std
    A1.append(ele)

a2 = a2
a2_mean = (a2 * 57) / 57
a2_std = np.std(a2)
A2 = []
for ele in a1: 
    ele = (ele - a2_mean) / a2_std
    A2.append(ele)

a3 = a3
a3_mean = (a1 * 57) / 57
a3_std = np.std(a1)
A3 = []
for ele in a3: 
    ele = (ele - a3_mean) / a3_std
    A3.append(ele)

a4 = a4
a4_mean = (a4 * 57) / 57
a4_std = np.std(a4)
A4 = []
for ele in a4: 
    ele = (ele - a4_mean) / a4_std
    A4.append(ele)

a5 = a5
a5_mean = (a5 * 57) / 57
a5_std = np.std(a5)
A5 = []
for ele in a5: 
    ele = (ele - a5_mean) / a5_std
    A5.append(ele)


print(a1.shape)
print(y.shape)