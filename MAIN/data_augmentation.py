from matplotlib import pyplot as plt
from sklearn import linear_model
import pandas as pd
import numpy as np
import pickle


pickle_in = open("/Users/akaash/Desktop/Projects/FF/ASSETS/X_train.pickle", "rb")
X_train = pickle.load(pickle_in)

pickle_in = open("/Users/akaash/Desktop/Projects/FF/ASSETS/Y_train.pickle", "rb")
Y_train = pickle.load(pickle_in)







