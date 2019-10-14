from statistics import mean
from sklearn import preprocessing
import pandas
import matplotlib.pyplot as plt

def slope(xs, ys):
    """
        Calculate and return the slope of the best-fit-line

        Parameters
        ----------
        xs : array-like or sparse matrix
            x values

        ys : array_like
            y values

        Returns
        -------
        Returns a number
        """
    mxmy = mean(xs)*mean(ys)
    mxy = mean(xs*ys)
    smx = mean(xs)**2
    msx = mean(xs**2)
    m = (mxmy - mxy) / (smx - msx)
    return m



def normalize_dataframe(df):
    x = df.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    return pandas.DataFrame(x_scaled, columns=df.columns)

def plot_dataframe(df):
    df.plot(kind='bar',figsize=(10,8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()