import pandas as pd
import numpy as np
import statistics

# Import and Clean Time Series
dataset = pd.read_csv("CumulativeCases.csv")

dates = dataset['Date']
colombia_dataset = dataset['Colombia']
belgium_dataset = dataset['Belgium']


#### Measures of Central Tendency
#### MEAN ###
mean_colombia = colombia_dataset.mean()
mean_belgium = belgium_dataset.mean()

#### MEDIAN
median_colombia = colombia_dataset.median()
median_belgium = belgium_dataset.median()

#### MODE
mode_colombia = colombia_dataset.mode()
mode_belgium = belgium_dataset.mode()

### MEASURES OF SPREAD
variance_colombia = statistics.variance(list(colombia_dataset))
variance_belgium = statistics.variance(list(belgium_dataset))

pvariance_colombia = statistics.pvariance(list(colombia_dataset))
pvariance_belgium = statistics.pvariance(list(belgium_dataset))

stdev_colombia = statistics.stdev(list(colombia_dataset))
stdev_belgium = statistics.stdev(list(belgium_dataset))

pstdev_colombia = statistics.pstdev(list(colombia_dataset))
pstdev_belgium = statistics.pstdev(list(belgium_dataset))

# Write Results into XSLX File

# Create lists from the datasets.
list_colombia = list(colombia_dataset)
list_belgium = list(belgium_dataset)

data1 = {
    'Measures of Central Tendency' : ['Mean', 'Median', 'Mode'],
    'Belgium': [int(mean_belgium), int(median_belgium), int(mode_belgium)],
    'Colombia' : [int(mean_colombia), int(median_colombia), int(mode_colombia)],
}

data2 = {
    'Measures of Spread' : ['Variance', 'Population Variance', 'Standard Deviation', 'Population Standard Deviation'],
    'Belgium' : [int(variance_belgium), int(pvariance_belgium), int(stdev_belgium), int(pstdev_belgium)],
    'Colombia' : [int(variance_colombia), int(pvariance_colombia), int(stdev_colombia), int(pstdev_colombia)]
}

df1 = pd.DataFrame(data1, columns = ['Measures of Central Tendency', 'Belgium', 'Colombia'])
df2 = pd.DataFrame(data2, columns = ['Measures of Spread', 'Belgium', 'Colombia'])

df1.to_excel('cent_tend.xlsx', index=False, header=True)
df2.to_excel('spread.xlsx', index=False, header=True)


