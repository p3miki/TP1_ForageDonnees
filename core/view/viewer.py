import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
import numpy as np


def update_view(data_frame):
    """Plots a graphs with the data provided"""
    # df['Year'] = df['Year'].astype(int)
    afficher_regions(data_frame)
    afficher_globales(data_frame)


def afficher_globales(data_frame):
    """Prints the global sales graph"""
    dff = data_frame.groupby(['Genre'])['Global_Sales'].sum()
    dff.plot(kind='bar', rot=1)
    plt.xlabel('Nombre Ventes Globales')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes globales')
    plt.show()


def afficher_regions(data_frame):
    """Prints sales graph by region
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    years = data_frame['Year'].unique()
    years.sort()
    dff = data_frame.groupby(['Year'])\
        .agg({'NA_Sales': 'sum', 'EU_Sales': 'sum', 'JP_Sales': 'sum', 'Other_Sales': 'sum'})
    dff.plot(kind='bar', rot=1)
    plt.xlabel('Région De Vente')
    plt.xticks(np.arange(len(years)), pd.Series(years).apply(lambda x: "" if x % 4 else x))
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes par région')
    plt.show()
