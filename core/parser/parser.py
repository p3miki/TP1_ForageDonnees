import pandas


def parse_data(data_frame):
    """Used to filter the data before returning the data frame
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_frame.dropna(inplace=True)
    data_frame = data_frame.loc[data_frame['Year'] != 2020]
    data_frame = data_frame.loc[data_frame['Year'] != 2017]

    return data_frame
