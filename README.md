Novel Python solutions to end-of-chapter statistics problems from the 4th Ed. of '**Medical Statistics**' from *Campbell, Machin, and Walters*. 

## Chapter 2 : Displaying Categorical Data    
### Clustered bar chart, thromboembolic women by blood type    
```Python3

import pandas as pd
import matplotlib.pyplot as plt

#Set File Path
file_path = '...thrombo.csv'
#Read CSV File from file_path
df = pd.read_csv(file_path)
#Set index to blood type
df = df.set_index('Blood_Group')
#Set plot style bar, title, figure size, legend, font size
df.plot(kind='bar', title ="Blood Type VS Thromboembolism",figsize=(10,5),legend=True, fontsize=12)
#rotate x-axis label, blood types
plt.xticks(rotation='horizontal')
#display plot
plt.show()
```
## Chapter 3 : Displaying Quantitative Data   
```Python3
"""
3.6 Exercises

1. Given a sample of ages (discrete years) of motor cyclists mortally injured in accidents
sample_data = [18, 41, 24, 28, 71, 52, 15, 20, 21, 31, 16, 24, 33, 44, 20, 24, 16, 64, 24, 18, 20, 21, 23, 22, 32]

(i) Draw a dot plot and histogram. Is distribution symmetric or skewed?
(ii) Calculate the mean, median, mode.
(iii) Calculate Range, Inter-quartile range, and Standard deviation
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from bokeh.plotting import figure, show
from collections import Counter

SAMPLE_DATA = [18, 41, 24, 28, 71, 52, 15, 20, 21, 31, 16, 24, 33, 44, 20, 24, 16, 64, 24, 18, 20, 21, 23, 22, 32]
```

### Dot Plot, Bar Chart of Ages of Motor Cyclists mortally injured in accidents    
**Dot Plot**: Solution using Bokeh, allows user to hover over data points to display values    
**Bar Chart**: Solution using MatPlotLib to generate binned age ranges.     
```Python3
def exercise_i(data):
    """
    :param data: list of age of expiration due to motorcycle accidents
    """
    def get_counts(data_to_count):
        counted_data = Counter(data_to_count)
        factors = list(counted_data.keys())
        counts = list(counted_data.values())
        return factors, counts

    # Get counts
    factors, counts = get_counts(data)
    
    # Build Dot Plot
    dot_plot = figure(title="Ages of Motorcyclists Critically Injured", tools="hover", toolbar_location=None,
                      y_range=[0,max(counts)+1],  x_range=[0, 100])
    dot_plot.circle(y=counts,x=factors, size=10, fill_color="red", line_color="black", line_width=3)

    #Convert data to DataFrame for MatPlotLib Histogram
    df = pd.DataFrame(data)

    # Create bin, ages 0 to 100, intervals of 5
    bin_range = range(0,100,5)
    
    # Construct Histogram Plot, apply a grid, set bins, remove unnecessary legend
    df.plot.hist(grid=True, bins=bin_range,
                       color='#607c8e', legend=False)
    
    # Add title, x and y axis labels
    plt.title("Ages of Motorcyclists Critically Injured")
    plt.xlabel("Ages")
    plt.ylabel("Counts")
    
    # Apply X-axis ticks, 5 year ranges
    plt.xticks(bin_range)

    # Generate plots
    plt.show()
    show(dot_plot)

exercise_i(SAMPLE_DATA)
```
#### Bokeh Dot Plot Output    
<img src="https://github.com/ajh1143/MedicalStatistics/blob/master/Chapter_3/Images/e_i_bokeh.png" class="inline"/><br>
#### MatPlotLib Histogram Output    
<img src="https://github.com/ajh1143/MedicalStatistics/blob/master/Chapter_3/Images/ei_hist.png" class="inline"/><br>

### Calculate Mean, Median, Mode    
**Mean** Numpy Solution: numpy.mean(data)    
**Median** Numpy Solution: numpy.median(data)    
**Mode** SciPy Solution: scipy.stats.mode(int(data[0])) - access index 0 for key of mode value, convert to int to remove `[]` delimiter
```Python3
    
def exercise_ii(data):
    data_mean = np.mean(data)
    data_median = np.median(data)
    data_mode = stats.mode(data)
    mode_output = int(data_mode[0])
    print("Mean:{}\nMedian:{}\nMode:{}".format(data_mean, data_median, mode_output))
 
 exercise_ii(SAMPLE_DATA)
 ```
 #### Mean, Median, Mode Output    
<img src="https://github.com/ajh1143/MedicalStatistics/blob/master/Chapter_3/Images/e_ii.png" class="inline"/><br>

 ### Calculate Range, Inter-quartile Range, Standard Deviation    
 **Range** NumPy Solution: numpy.abs(max(data) - min(data))    
 **IQR** SciPy Solution scipy.stats.iqr(data)    
 **SD** NumPy Solution: numpy.std(data)    
```Python3
def exercise_iii(data):
    data_range = np.abs(max(data) - min(data))
    data_quartiles = stats.iqr(data)
    data_sd = np.std(data)
    print("Range:{}\nInterquartile Range:{}\nStandard Deviation:{}".format(data_range, data_quartiles, data_sd))

exercise_iii(SAMPLE_DATA)
```
 ####  Range, Inter-quartile Range, Standard Deviation Output  
<img src="https://github.com/ajh1143/MedicalStatistics/blob/master/Chapter_3/Images/e_iii.png" class="inline"/><br>
