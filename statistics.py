import pandas as pd
import plotting
import calendar
import utils.util as util

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

def shape_of_UFO(data_df):
    """
    Given pandas dataframe, this method will return the top 10 as a string.
    """
    # Counts all occurances of unique words in column, and indexes them
    df = data_df['shape'].value_counts().reset_index()
    
    # Get the top 10 values and cast to list of lists
    shape_top_ten_list = df[:10].values.tolist()

    # map the list to contain formatted strings, then join it to single string with new lines.
    return '\n'.join(map(lambda l : f'{l[0]} mentioned: {l[1]} times', shape_top_ten_list))

def sigthing_length_of_ufo(data_df):
    data_df['duration(seconds)'] = pd.to_numeric(data_df["duration(seconds)"], errors='coerce')
    total = data_df['duration(seconds)'].sum()
    minutes = (total / data_df.size / 60).astype(int)
    seconds = (total / data_df.size % 60).astype(int)
    return f'{minutes} minutes and {seconds} seconds'

def days_probability_of_UFO_sighting(data_df):
    days = data_df['datetime'].dt.dayofweek.value_counts(normalize = True).sort_index().map(lambda d: d * 100)
    plotting.plot_days_probability_of_UFO_sighting(days)


def polarity_sentiment_plot(data_df):
    """
    Given pandas dataframe, runs Sentiment analasys on the comments of the experience,
    then creates a plot with the data.
    """
    # Run the sentiment analasys on the comments, and add it as a row to the dataframe
    data_df['sentiment'] = data_df['comments'].apply(util.sentiment_calc)
    
    # Create and add to new dataframe the values of the NamedTuple Sentiment (datatype of TextBlob analysis)
    sentiment_df = pd.DataFrame(columns=['polarity', 'subjectivity'])
    
    # Unpack the values to columns in dataframe 
    # zip(*) the * means that it will run through all arguments in the column and unpack them
    sentiment_df['polarity'], sentiment_df['subjectivity'] = zip(*data_df.sentiment)
    
    # Create lists to be used for plotting
    polarity = sentiment_df['polarity'].values.tolist()
    subjectivity = sentiment_df['subjectivity'].values.tolist()

    plotting.plot_sentiment_polarity_per_case(polarity, subjectivity)