import pandas as pd
import argparse
import matplotlib.pyplot as plt

## Q1
## Output the scatterplot

task2_data = pd.read_csv("owid-covid-data-2020-monthly.csv", encoding = 'ISO-8859-1')

# Store all the location 
location_list = set(task2_data['location'])

# Plot a scatter plot by location
for location in location_list :
    loc = task2_data.loc[task2_data['location']==location]
    plt.scatter(loc.iloc[:,2], loc.iloc[:,4], label=loc)

plt.ylabel("case fatality rate")
plt.xlabel("confirmed new cases")

plt.savefig('scatter-a.png')
