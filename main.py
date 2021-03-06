import pandas as pd
import numpy as np
import statistics
import utils.downloader as downloader
"""
To run ´$python main.py´
"""
def date_parser(date_to_parse):
    return pd.to_datetime(date_to_parse, format="%m/%d/%Y", exact=False)

if __name__ == '__main__':
    file_name = 'ufo_data.csv'

    # Download file
    downloader.download_as_file(file_name)

    data_df = pd.read_csv(file_name, low_memory=False, encoding='utf8',
                          names=['datetime', 'city', 'state', 'country',
                                 'shape', 'duration(seconds)', 'duration (hours/min)',
                                 'comments', 'date posted', 'latitude', 'longitude']
                             , parse_dates=['datetime'], date_parser=date_parser)

# # 1. Hvilket sted er der flest UFO observationer?
print('1. Hvilket sted er der flest UFO observationer?')
res = statistics.most_UFOs_observed(data_df)
print(
    f'Stedet med flest UFO obserervationer er {res[0]} med {res[1]} observationer\n')

#2. Hvordan har antallet af observationer udviklet sig over tid? ####### THIS SHOULD BE A PLOT ###########
print("2. Hvordan har antallet af observationer udviklet sig over tid?  - Se plot")
statistics.observations_per_year(data_df)

# # 3. Hvornår på året er der flest observationer?

month = statistics.month_with_most_observations(data_df)
print("3. Hvornår på året er der flest observationer?")
print(f'Måneden med flest observationer er {month}')

# # 4. Hvordan ser en ufo ud?
print('4. Hvordan ser en ufo ud?\n')
shapes = statistics.shape_of_UFO(data_df)
print(f'Top 10 former af UFO\'er er :\n{shapes}')

# # 5. Hvor lang tid kunne de se ufoen(gennemsnit)?
print("5. Hvor lang tid kunne de se ufoen(gennemsnit)")
timespan = statistics.sigthing_length_of_ufo(data_df)
print(f'Gennemsnitlig UFO set tid: {timespan}')

# #  6. På hvilke dage er det sandsynligt at se ufoer(i procentvis fordeling)?
statistics.days_probability_of_UFO_sighting(data_df)

# # 7. Lav en graf over polaritet og sentiment.
statistics.polarity_sentiment_plot(data_df)

# # 8. Lav et plot, der viser antallet af ufo observationer pr stat i USA, og farvekode jeres resultat. 
statistics.UFO_observation_per_state(data_df)