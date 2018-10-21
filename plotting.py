import matplotlib.pyplot as plt

def plot_days_probability_of_UFO_sighting(days):
    x_values = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']  
    plt.xlabel('days')
    plt.ylabel('percentage')
    plt.bar(x_values,days)
    plt.show()

def plot_bar(values, freq, x_label, y_label='frequency'):
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