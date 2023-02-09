import pandas as pd
import numpy as np
import pickle
import random

Msia_cal_per_day = np.array([])
data1 = pd.read_csv("/Users/akaash/Desktop/Projects/FFV3/ASSETS/daily-per-capita-caloric-supply.csv")
df1 = pd.DataFrame(data1)
for i in range(0, len(df1)):
    Msia_cal_per_day = np.append(Msia_cal_per_day, df1.values[i][3])

pickle_out = open("Msia_cal_per_day.pickle", "wb")
pickle.dump(Msia_cal_per_day, pickle_out)
pickle_out.close()

Msia_chicken_consumption_yearly = np.array([])
data2 = pd.read_csv("/Users/akaash/Desktop/Projects/FFV3/ASSETS/FAOSTAT_data_en_2-9-2023.csv")
df2 = pd.DataFrame(data2)
for i in range(0, len(df2)):
    #Msia_cal_per_day = np.append(Msia_cal_per_day, df1.values[i][3])
    Msia_chicken_consumption_yearly = np.append(Msia_chicken_consumption_yearly, (1000 * df2.values[i][11]))

pickle_out = open("Msia_chicken_consumption_yearly.pickle", "wb")
pickle.dump(Msia_chicken_consumption_yearly, pickle_out)
pickle_out.close()

Msia_political_instability = []
for i in range(1961, 2019):
    Msia_political_instability.append(random.randint(0, 40))
print(Msia_political_instability)


