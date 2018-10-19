import pandas as pd
import plotting
import calendar
##  headers ['datetime', 'city', 'state', 'country', 'shape', 'duration (seconds)', 'duration (hours/min)', 'comments', 'date posted', 'latitude', 'longitude']

def most_UFOs_observed(data_df):
    """
    Given pandas dataframe, return an list with city on first(0) index and count on second(1) index
    """
    ##Create list of unique country values
    df = data_df['city'].value_counts().reset_index()
    ## return the first row, as the data is descending.
    return df[:1].values[0]

def observations_per_year(data_df):
    """
    Given pandas dataframe, this method will create a plot of the count of sightings per year.
    """
    print(type(data_df['datetime'][2]))
    # mask = data_df[data_df['datetime']
    # pd.value_counts()

def month_with_most_observations(data_df):
    month = data_df['datetime'].groupby([data_df['datetime'].dt.month]).count()
    return [calendar.month_name[month.idxmax()], month.loc[month.idxmax()]]

def sigthing_length_of_ufo(data_df):
    data_df['duration(seconds)'] = pd.to_numeric(data_df["duration(seconds)"], errors='coerce')
    total = data_df['duration(seconds)'].sum()
    return (total / data_df.size).astype(int)