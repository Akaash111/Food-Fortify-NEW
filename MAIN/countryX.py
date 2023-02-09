#data for country A
import random
import numpy as np
import os
import pickle


DATA = []
REL_SCORES = []
DATA_DIR = "/Users/akaash/Desktop/Projects/FF/ASSETS"

#data contains arrays of feature values for country A over the past 40 months

for _ in range(0, 40):

    a1 = random.random()
    a2 = random.random()
    a3 = random.random()
    a4 = random.random()
    a5 = random.random()
    a6 = random.random()

    monthly_data = [a1, a2, a3, a4, a5, a6]

    DATA.append(monthly_data)

#print(DATA[0])

#calc reliability score for each year

for year in DATA:
    
    rel = (year[3] * year[5]) / (year[0] * year[1] * year[3] * year[5])

    REL_SCORES.append(rel)

print(REL_SCORES)

pickle_out = open("X_train.pickle", "wb")
pickle.dump(DATA, pickle_out)
pickle_out.close()

pickle_out = open("Y_train.pickle", "wb")
pickle.dump(REL_SCORES, pickle_out)
pickle_out.close()
