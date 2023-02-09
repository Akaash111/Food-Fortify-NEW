#data for country A
import random
import numpy as np

class data_CountryX():

    def __init__(self):
        self.data = np.array([])

        #data contains arrays of feature values for country A over the past 40 months

        for _ in range(0, 40):

            a1 = random.random()
            a2 = random.random()
            a3 = random.random()
            a4 = random.random()
            a5 = random.random()
            a6 = random.random()

            monthly_data = np.array([a1, a2, a3, a4, a5, a6])
            data = np.append(self.data, monthly_data)

            print(self.data)
        
        #calc reliability score for each year

        for year in self.data:
            print(year[3])
            rel = (year[3] * year[5]) / (year[0] * year[1] * year[3] * year[5])

            print(rel)


init = data_CountryX()