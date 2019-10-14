import pandas
from labels import school
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from statistics import mean
import numpy as np
from tools import slope, normalize_dataframe, plot_dataframe
from MultivariateLR import MultivariateLR
from statistics import mean


def main():
    df = pandas.read_csv('./casted_data/casted.csv')
    # df = normalize_dataframe(df)
    predict_column = 'G3'
    X = df.drop(predict_column, axis=1)
    y = df[predict_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = MultivariateLR()
    model.fit(X_train, y_train)
    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)
    _slopes = model.get_slope()
    print(model.get_intercept())
    print('__slopes___')
    for s1, s2, x in zip(_slopes, regressor.coef_, X_train.values[0]):
        print(f'{s1} -- {s2} -- {x} -- {mean(y_train)}')
    # plot_dataframe(pandas.DataFrame({'Mine': _slopes, 'Sklearn': regressor.coef_}), )
    return
    # n = len(X)
    # # for column in range(n):
    # print(X.values[0])
    # labels = [i for i in df.columns]
    # print(labels)
    # # for l in labels[:3]: 
    # #     print(df[l])

    # xs = df['health']
    # ys = df['G3']
    # m = slope(xs, ys)
    # print(m)
    # # return


    # X = df.drop(predict_column, axis=1)
    # y = df[predict_column]



    
    # plot_data
    # y_pred = regressor.predict(X_test)
    # # # df1 = pandas.DataFrame({'Actual': y_test, 'Predicted': y_pred})


main()