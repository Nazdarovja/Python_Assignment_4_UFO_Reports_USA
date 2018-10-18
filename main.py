import pandas as pd
import statistics
import utils.downloader as downloader


if __name__ == '__main__':
    file_name = 'ufo_data.csv'

    # Download file
    downloader.download_as_file(file_name)

    # Get file as pandas csv and add missing header column
    data_df = pd.read_csv(file_name, low_memory=False, encoding='utf8',
                          names=['datetime', 'city', 'state', 'country',
                                 'shape', 'duration (seconds)', 'duration (hours/min)',
                                 'comments', 'date posted', 'latitude', 'longitude'])

#1. Hvilket sted er der flest UFO observationer?
print('Hvilket sted er der flest UFO observationer?')
res = statistics.most_UFOs_observed(data_df)
print(f'Stedet med flest UFO obserervationer er {res[0]} med {res[1]} observationer')

#2. Hvordan har antallet af observationer udviklet sig over tid? ####### THIS SHOULD BE A PLOT ###########

#3. Hvornår på året er der flest observationer?

#4. Hvordan ser en ufo ud?

#5. Hvor lang tid kunne de se ufoen(gennemsnit)?
