import re
import sys
import pandas as pd
import numpy as np
import nltk
import os
import glob

# Search the textfile that contains 3 given keywords and output the corresponding IDs
def search(word1, word2, word3) :
    
    # Store all the text files in 'files'
    files = []
    for textfile in glob.glob("./cricket/*.txt"):
        files.append(textfile)
    
    # Find the text file that contains all three keywords
    matched_file = []
    for file in files:
        infile = open(file, 'r')
        lines = infile.readlines()
        if (re.search(r'\b'+word1+r'\b', str(lines))) and (re.search(r'\b' + word2 + r'\b', str(lines))) and (re.search(r'\b' + word3 + r'\b', str(lines))) :
            matched_file.append(file)

    # Load 'partb1.csv' and search for corresponding filename and IDs
    filename_id_data = pd.read_csv("partb1.csv", encoding = 'ISO-8859-1')
    index = []   # index of the filename in csv that contains 3 keywords
    for file in matched_file :
        for filename in filename_id_data['filename']:
            a, b = os.path.splitext(filename)
            if a in file :
                index.append(filename_id_data.index[filename_id_data['filename']==file].tolist())
    index = np.array(index).flatten()
    
    # Store the document IDs that match the text files
    matched_id = []
    for i in index:
        matched_id.append(filename_id_data.iloc[i,1])
    
    return matched_id
