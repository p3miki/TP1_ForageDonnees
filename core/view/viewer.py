import os

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def update_view(data_frame):
    """Plots the graphs with the data provided"""
    afficher_regions(data_frame)
    afficher_globales(data_frame)
    afficher_consoles(data_frame)


def afficher_globales(df):
    dff = df.groupby(['Genre'])['Global_Sales'].sum().sort_values()
    dff.plot(kind='bar', rot=1)
    plt.xlabel('Genres de jeu')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes totales par Genres')
#    _maximize(plt.get_current_fig_manager(), plt)
    plt.show()

def afficher_consoles(df):
    dff = df.groupby(['Platform'])['Global_Sales'].sum().sort_values()
    dff.plot(kind='bar', rot=1)
    plt.xlabel('Nom de Console')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes par Console')
    plt.show()

def afficher_regions(data_frame):
    """Prints sales graph by region
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    years = data_frame['Year'].unique()
    years.sort()
    dff = data_frame.groupby(['Year']) \
        .agg({'NA_Sales': 'sum', 'EU_Sales': 'sum', 'JP_Sales': 'sum', 'Other_Sales': 'sum'})
    dff.plot(rot=1)
    plt.xlabel('Région De Vente')
#    plt.xticks(np.arange(len(years)), pd.Series(years).apply(lambda x: "" if x % 4 else x))
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes par région')
#    _maximize(plt.get_current_fig_manager(), plt)
    plt.show()


#def _maximize(manager, plotter):
#    if os.uname().sysname == "Linux" and plotter.get_backend() == "TkAgg":
#        manager.resize(*manager.window.maxsize())
#    elif plotter.get_backend() == "TkAgg":
#        manager.window.state('zoomed')
#    elif plotter.get_backend() == "wxAgg":
#        manager.frame.Maximize(True)
#    elif plotter.get_backend() == "Qt4Agg":
#        manager.window.showMaximized()
