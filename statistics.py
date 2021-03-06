import pandas as pd
import plotting
import calendar
import utils.util as util
import folium as folium
import json

##  headers ['datetime', 'city', 'state', 'country', 'shape', 'duration (seconds)', 'duration (hours/min)', 'comments', 'date posted', 'latitude', 'longitude']


def most_UFOs_observed(data_df):
    """
    Given pandas dataframe, returns a list with city on first(0) index and count on second(1) index
    """
    # Create list of unique country values
    df = data_df['city'].value_counts().reset_index()
    # return the first row, as the data is descending.
    return df[:1].values[0]


def observations_per_year(data_df):
    """
    Given pandas dataframe, this method creatse a plot of the count of sightings per year.
    """
    # Gets each year present and then groups them and counts all occurances.
    ps = data_df['datetime'].groupby([data_df['datetime'].dt.year]).count()
    
    # Cast data to list for plotting
    values = ps.keys().tolist()
    freq = ps.values.tolist()
    plotting.plot_bar(values,freq,'year')


def month_with_most_observations(data_df):
    """
    Given pandas dataframe, this method returns the month with most observations and the count of observations.
    """
    # Gets each month present and then groups them and counts all occurances.
    month = data_df['datetime'].groupby([data_df['datetime'].dt.month]).count()
    return [calendar.month_name[month.idxmax()], month.loc[month.idxmax()]]


def shape_of_UFO(data_df):
    """
    Given pandas dataframe, this method returns the top 10 as a string.
    """
    # Counts all occurances of unique words in column, and indexes them
    df = data_df['shape'].value_counts().reset_index()

    # Get the top 10 values and cast to list of lists
    shape_top_ten_list = df[:10].values.tolist()

    # map the list to contain formatted strings, then join it to single string with new lines.
    return '\n'.join(map(lambda l: f'{l[0]} mentioned: {l[1]} times', shape_top_ten_list))


def sigthing_length_of_ufo(data_df):
    """
    Given pandas dataframe, this method returns the avarage observation time of a UFO.
    """
    # Cast column to numeric values and change the errors to NaN
    data_df['duration(seconds)'] = pd.to_numeric(
        data_df["duration(seconds)"], errors='coerce')
    
    # Calculate to minutes and seconds instead of sec
    total = data_df['duration(seconds)'].sum()
    minutes = (total / data_df.size / 60).astype(int)
    seconds = (total / data_df.size % 60).astype(int)
    return f'{minutes} minutes and {seconds} seconds'

def days_probability_of_UFO_sighting(data_df):
    """
    Given pandas dataframe, this method will plot weekday probability of UFO sightings.
    """
    # Counts all occurances of the given weekday, then gets the relative values (normalize = True) 
    # Then runs through the values and times them by 100, so we have them in percent
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
    sentiment_df['polarity'], sentiment_df['subjectivity'] = zip(
        *data_df.sentiment)

    # Create lists to be used for plotting
    polarity = sentiment_df['polarity'].values.tolist()
    subjectivity = sentiment_df['subjectivity'].values.tolist()

    # plotting.plot_sentiment_polarity_per_case(polarity, subjectivity)
    plotting.plot_sentiment_polarity_per_case(polarity, subjectivity)


def UFO_observation_per_state(data_df):
    """
    Given pandas dataframe, shows observations per state on a map using Folium; 
    each state colorcoded according to amount of observations.
    """

    # load GeoJSON geometries for USA 
    with open('us-states.json') as data_file:
        my_USA_map = json.load(data_file)

    # select data from USA only, and sort/count observation by state
    from_us = data_df[data_df["country"] == "us"]
    df = from_us['state'].value_counts().reset_index()

    # instantiate a Folium map 
    map = folium.Map(location=[48, -102], zoom_start=3)

    # apply geoJSON overlay on the map
    map.choropleth(geo_data=my_USA_map, data=df,
                   columns=['index','state'],  
                   key_on='feature.id',
                   legend_name="UFO observations per state",
                   fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
                   highlight=True)

    # save map as html
    map.save('plots_8.html')
