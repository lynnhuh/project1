import pandas as pd
import argparse
import re

## Q1
## Aggregate the values by 'month' and 'location' in the year 2020.

covid_data = pd.read_csv("owid-covid-data.csv", encoding = 'ISO-8859-1')
task1 = covid_data.loc[:,['location','date','total_cases','new_cases','total_deaths','new_deaths']] 
task1 = task1.dropna()

# Drop the rows of 2021 data using regular expression
date_pattern = r'^2020-\d{2}-\d{2}$'
for date in task1['date'] :
    if not re.search(date_pattern, date) :
        index = task1.index[task1['date'] == date].tolist()
        task1 = task1.drop(index)

# Change the name of column 'date' to 'month'
task1.columns = ['month' if column=='date' else column for column in task1.columns]

# Extract month from date data
for date in task1['month']:
    split = date.split('-')
    month = re.sub(date_pattern, split[1], date)
    task1 = task1.replace(date, month)
    
print(task1)

## Q2
## Add a new header column 'case_fatality_rate'

# Convert to numeric values
task1['total_cases'] = pd.to_numeric(task1['total_cases'])
task1['new_cases'] = pd.to_numeric(task1['new_cases'])
task1['total_deaths'] = pd.to_numeric(task1['total_deaths'])
task1['new_deaths'] = pd.to_numeric(task1['new_deaths'])

# Calculate case fatality rate (number of cases)/(number of deaths)
# Store them in a list 'rate'
rate = []
for index, data in task1.iterrows() :
    value = (data['total_cases']+data['new_cases']) / (data['total_deaths']+data['new_deaths'])
    rate.append(value)

# Add a new column 'case_fatality_rate' and sort in an ascending order
task1.insert(2, 'case_fatality_rate', rate)
task1 = task1.sort_values(by=['case_fatality_rate'])
task1.to_csv(r'owid-covid-data-2020-monthly.csv', index=False)
print(task1.head())
