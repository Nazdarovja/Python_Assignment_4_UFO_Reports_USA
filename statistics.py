import pandas as pd

##  headers ['datetime', 'city', 'state', 'country', 'shape', 'duration (seconds)', 'duration (hours/min)', 'comments', 'date posted', 'latitude', 'longitude']

def most_UFOs_observed(data_df):
    """
    Given pandas dataframe, return an list with city on first(0) index and count on second(1) index
    """
    ##Create list of unique country values
    df = data_df['city'].value_counts().reset_index()
    ## return the first row, as the data is descending.
    return df[:1].values[0]