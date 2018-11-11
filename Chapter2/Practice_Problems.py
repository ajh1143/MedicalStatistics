## Clustered bar chart, thromboembolic women by blood type

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
