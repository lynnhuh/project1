import re
import pandas as pd
import numpy as np
import os
import glob
import sys
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Using PorterStemmer(), find the IDs that has stem words of keywords
def porterstemmer(word1, word2, word3) :
    
    porterStemmer = PorterStemmer()
    
    # Store all the text files in 'files'
    files = []
    for textfile in glob.glob("./cricket/*.txt"):
        files.append(textfile)
    
    # Find the text file that has stem words of 3 keywords
    matched_file = []
    for file in files:
        stemWords = []
        infile = open(file, 'r')
        lines = infile.readlines()
        words = word_tokenize(lines[0])
        # Create a dictionary to count how many stem words are found
        wordDict = {}
        for word in words:
            stemWord = porterStemmer.stem(word)
            if stemWord in wordDict :
                wordDict[stemWord] = wordDict[stemWord] + 1
            else :
                wordDict[stemWord] = 1
        
        if (porterStemmer.stem(word1) in wordDict.keys()) and (porterStemmer.stem(word2) in wordDict.keys()) and (porterStemmer.stem(word3) in wordDict.keys()) :
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
        
    return matched_id, matched_file

matched_id, matched_file = porterstemmer(sys.argv[1], sys.argv[2], sys.argv[3])
print(matched_id)
