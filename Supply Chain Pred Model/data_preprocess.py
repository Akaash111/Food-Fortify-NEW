import pandas as pd
import numpy as np
import pickle
import random

Msia_cal_per_day = np.array([])
data1 = pd.read_csv("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/ASSETS/daily-per-capita-caloric-supply.csv")
df1 = pd.DataFrame(data1)
for i in range(0, len(df1)):
    Msia_cal_per_day = np.append(Msia_cal_per_day, df1.values[i][3])
pickle_out = open("Msia_cal_per_day.pickle", "wb")
pickle.dump(Msia_cal_per_day, pickle_out)
pickle_out.close()



Msia_chicken_consumption_yearly = np.array([])
data2 = pd.read_csv("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/ASSETS/FAOSTAT_data_en_2-9-2023.csv")
df2 = pd.DataFrame(data2)
for i in range(0, len(df2)-1):
    #Msia_cal_per_day = np.append(Msia_cal_per_day, df1.values[i][3])
    Msia_chicken_consumption_yearly = np.append(Msia_chicken_consumption_yearly, (1000 * df2.values[i][11]))
pickle_out = open("Msia_chicken_consumption_yearly.pickle", "wb")
pickle.dump(Msia_chicken_consumption_yearly, pickle_out)
pickle_out.close()




Msia_exchange_rates = np.array([])
data3 = pd.read_csv("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/ASSETS/Sorted exchange rate.csv")
df3 = pd.DataFrame(data3)
for i in range(5, 62):
    Msia_exchange_rates = np.append(Msia_exchange_rates, df3.values[5][i])
    #shape 58,
pickle_out = open("Msia_exchange_rates.pickle", "wb")
pickle.dump(Msia_exchange_rates, pickle_out)
pickle_out.close()



Msia_inflation_data = np.array([])
data4 = pd.read_csv("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/ASSETS/Sorted Inflation.csv")
df4 = pd.DataFrame(data4)
for i in range(3, 60):
    Msia_inflation_data = np.append(Msia_inflation_data, df4.values[5][i])
    #shape 58, 
pickle_out = open("Msia_inflation_data.pickle", "wb")
pickle.dump(Msia_inflation_data, pickle_out)
pickle_out.close()


Msia_labour_data = np.array([])
data5 = pd.read_csv("/Users/akaash/Desktop/Projects/FF/Supply Chain Pred Model/ASSETS/Sorted Labour.csv")
df5 = pd.DataFrame(data5)
for i in range(4, 61):
    Msia_labour_data = np.append(Msia_labour_data, df5.values[5][i])
    #shape 58,
pickle_out = open("Msia_labour_data.pickle", "wb")
pickle.dump(Msia_labour_data, pickle_out)
pickle_out.close()



Msia_political_instability = []
for i in range(1961, 2018):
    Msia_political_instability = np.append(Msia_political_instability,random.randint(0, 40))
#print(Msia_political_instability)




