import pandas


def parse_data(data_frame):
    """:param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_top = data_frame.head(10)
    # iterating the columns
    #print(data_frame)
    return data_top
