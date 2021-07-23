import re
import pandas as pd
import numpy as np
import glob
import os

## Create a csv file

# Find a document ID using regex
def extract_id(text) :
    lines = text.readlines() # in list

    pattern = r'[A-Z]{4}-\d{3}[A-Z]?'
    
    for line in lines :
        if re.search(pattern, line):
            ID = re.findall(pattern,line)
    
    return ID

# Store all the text files in 'files'
files = []
for textfile in glob.glob("./cricket/*.txt"):
    files.append(textfile)

# Loop through each text file and store each ids in 'IDs'
IDs = []
for file in files :
    text = open(file, "r") 
    ID = extract_id(text)
    IDs.append(ID)
    
IDs_array = np.array(IDs)
IDs = IDs_array.flatten().tolist()

# Create a dataframe and convert to csv file
data = {'filename': files , 'documentID': IDs}
partb1 = pd.DataFrame(data=data)
partb1.to_csv(r'partb1.csv', index=False)
