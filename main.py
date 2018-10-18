import pandas as pd
import numpy as np
import statistics
import utils.downloader as downloader


if __name__ == '__main__':
    file_name = 'ufo_data.csv'

    # Download file
    downloader.download_as_file(file_name)

    ##    dtype={'datetime': str, 'city': str, 'state': str, 'country': str,
            #  'shape': str, 'duration (seconds)': np.float64, 'duration (hours/min)' : str,
            #  'comments' : str, 'date posted': str, 'latitude': float, 'longitude': float},
            #  date_parser = dt_conv , error_bad_lines=False
    # Get file as pandas csv and add missing header column 11/20/1995 19:12
    data_df = pd.read_csv(file_name, low_memory=False, encoding='utf8',
                          names=['datetime', 'city', 'state', 'country',
                                 'shape', 'duration (seconds)', 'duration (hours/min)',
                                 'comments', 'date posted', 'latitude', 'longitude']
                             )
    ## THIS DOES NOT WORK FOR SOME REASON 
    # ValueError: time data '10/11/2006 24:00' does not match format '%m/%d/%Y %H:%M
    #data_df['datetime'] = pd.to_datetime(data_df['datetime'], format="%m/%d/%Y %H:%M")


# 1. Hvilket sted er der flest UFO observationer?
print('Hvilket sted er der flest UFO observationer?')
res = statistics.most_UFOs_observed(data_df)
print(
    f'Stedet med flest UFO obserervationer er {res[0]} med {res[1]} observationer\n')

#2. Hvordan har antallet af observationer udviklet sig over tid? ####### THIS SHOULD BE A PLOT ###########
statistics.observations_per_year(data_df)
# 3. Hvornår på året er der flest observationer?

# 4. Hvordan ser en ufo ud?

# 5. Hvor lang tid kunne de se ufoen(gennemsnit)?
