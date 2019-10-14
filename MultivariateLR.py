from tools import slope
import numpy as np
import pandas
from statistics import mean

# y = b + x1.m1 + x2.m2 + ... + xn.mn
# b = my * m*mx = yBar - x1Bar*m1 - x2bar*m2 - ... - xnBar*mn
class MultivariateLR:
    def __init__(self):
        self.__slopes = []
        self.__intercept = 0

    def fit(self, X, y):
        n = len(X)
        self.__intercept = mean(y) #yBar
        for label in X:
            x_i_Bar = X[label]
            m = slope(x_i_Bar, y)
            self.__slopes.append(m)
            self.__intercept = self.__intercept - (m * mean(x_i_Bar))
        # print('__intercept__')
        # print(self.__intercept)

    @staticmethod
    def __preprocess_data(X):
        X = np.array(X)

    def __cal(self, Xi):
        intercept = self.__intercept
        slopes = self.__slopes
        y = intercept
        for mi, xi in zip(slopes, Xi):
            y = y + mi * xi
        return y

    def predict(self, X):
        self.__preprocess_data(X)
        ys = []
        for i in X:
            y = self.__cal(i)
            ys.append(y)
    
    def get_slope(self):
        return self.__slopes

    def get_intercept(self):
        return self.__intercept