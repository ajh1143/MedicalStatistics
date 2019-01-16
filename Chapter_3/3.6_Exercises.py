"""Chapter 3: Displaying Quantitative Data
3.6 Exercises

1. Given a sample of ages (discrete years) of motor cyclists mortally injured in accidents
sample_data = [18, 41, 24, 28, 71, 52, 15, 20, 21, 31, 16, 24, 33, 44, 20, 24, 16, 64, 24, 18, 20, 21, 23, 22, 32]

(i) Draw a dot plot and histogram. Is distribution symmetric or skewed?
(ii) Calculate the mean, median, mode.
(iii) Calculate the range, inter quartile range, and standard deviation.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from scipy import stats
from collections import Counter

SAMPLE_DATA = [18, 41, 24, 28, 71, 52, 15, 20, 21, 31, 16, 24, 33, 44, 20, 24, 16, 64, 24, 18, 20, 21, 23, 22, 32]

def exercise_i(data):
    """
    :param data: list of age of expiration due to motorcycle accident
    """
    #Create Dot Plot
    counted_data = Counter(data)
    factors = list(counted_data.keys())
    counts = list(counted_data.values())
    dot_plot = figure(title="Ages of Motorcyclists Critically Injured", tools="hover", toolbar_location=None,
                      y_range=[0,max(counts)+1],  x_range=[0, 100])
    dot_plot.circle(y=counts,x=factors, size=10, fill_color="red", line_color="black", line_width=3)

    #Convert data to DataFrame
    df = pd.DataFrame(data)

    #Plot Histogram
    df.plot.hist(grid=True, bins=10, rwidth=.75,
                   color='#607c8e', legend=False)
    plt.title("Ages of Motorcyclists Critically Injured")
    plt.xlabel("Ages")
    plt.ylabel("Counts")
    
    # Apply X-axis ticks, 5 year ranges
    plt.xticks(range(0, 100, 5))

    # Generate plots
    plt.show()
    show(dot_plot)

def exercise_ii(data):
    data_mean =np.mean(data)
    data_median = np.median(data)
    data_mode = stats.mode(data)
    mode_output = int(data_mode[0])
    print("Mean:{}\nMedian:{}\nMode:{}".format(data_mean, data_median, mode_output))    
    

def exercise_iii(data):
    data_range = np.abs(max(data) - min(data))
    data_quartiles = stats.iqr(data)
    data_sd = np.std(data)
    print("Range:{}\nInterquartile Range:{}\nStandard Deviation:{}".format(data_range, data_quartiles, data_sd))
    
exercise_i(SAMPLE_DATA)
exercise_ii(SAMPLE_DATA)
exercise_iii(SAMPLE_DATA)
