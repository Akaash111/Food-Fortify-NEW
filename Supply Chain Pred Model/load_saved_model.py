import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from data_preprocess import Msia_cal_per_day as a1

#ModelA1= keras.models.load_model("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/Saved Model/A1")
ModelA2= keras.models.load_model("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/Saved Model/A2")
ModelA3= keras.models.load_model("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/Saved Model/A3")
#ModelA4= keras.models.load_model("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/Saved Model/A4")
#ModelA5= keras.models.load_model("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/Saved Model/A5")


#TESTING
input_value = 1961 
y_hat = []
for i in range(1961, 2018):
    prediction = ModelA3.predict(np.array([i]).reshape(1, 1))
    y_hat.append(prediction)

x = []
for i in range(1961, 2018):
    x.append(i)

y_hat = np.array(y_hat)
y_hat.reshape(57, -1)
x = np.array(x)

print(x.shape)
print(y_hat.shape)

plt.plot(x, y_hat.reshape(57, -1))
plt.show()






