import matplotlib.pyplot as plt

def plot_days_probability_of_UFO_sighting(days):
    """
    Given list of values for each day, will show a plot.
    """
    # Day values for x axis
    x_values = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']  

    # Add labels and plot
    plt.xlabel('Days')
    plt.ylabel('Percentage')
    plt.bar(x_values,days)
    plt.show()

def plot_bar(values, freq, x_label, y_label='frequency'):
    """
    Given values, freq of values, and labels for plot, shows bar plot
    """
    # Set labels and plot
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.bar(values,freq)
    plt.show()

def plot_sentiment_polarity_per_case(polarity, subjectivity):
    """
    Given a list of ploarity values and subjectivity values, creates a plot for each index.
    """
    # Create polarity and subjectivity plot, and add smaller linewidth because there is ALOT of lines
    plt.plot(range(len(polarity)), polarity, linewidth=0.5, label='polarity')
    plt.plot(range(len(subjectivity)), subjectivity, linewidth=0.5, label='subjectivity')
    
    #Set labels and add legend and add grid
    plt.xlabel('Occurance number')
    plt.ylabel('Polarity(-1(negative) - 1(positive))\n Subjectivity(0-1)')
    plt.legend(loc='upper left')
    plt.grid()
    plt.title('Plot showing Polarity and Subjectivity')
    
    plt.show()