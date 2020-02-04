import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas


def update_view(df):
    """Plots a graphs with the data provided"""
    #df['Year'] = df['Year'].astype(int)
    afficher_regions(df)
    afficher_globales(df)

def afficher_globales(df):
    dff = df.groupby(['Genre'])['Global_Sales'].sum()
    dff.plot(kind='bar', rot=1)
    plt.xlabel('Nombre Ventes Globales')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes par région')
    plt.show()

def afficher_regions(df):
    dff = df.groupby(['Year']).agg({'NA_Sales': 'sum', 'EU_Sales': 'sum', 'JP_Sales': 'sum', 'Other_Sales': 'sum'})
    dff.plot(kind='bar', rot=1)
    plt.xlabel('Région De Vente')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes par région')
    plt.show()