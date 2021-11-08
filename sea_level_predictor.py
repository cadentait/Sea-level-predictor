import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    
    # Create scatter plot
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x1 = np.arange(df['Year'][0], 2051,1)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(x1, res.intercept + res.slope*x1, 'r')
    
    # Create second line of best fit
    x2_df = df[df['Year'] >= 2000]
    x2 = np.arange(2000,2051,1)
    res_2 = linregress(x2_df['Year'], x2_df['CSIRO Adjusted Sea Level'])
    plt.plot(x2, res_2.intercept + res_2.slope*x2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()