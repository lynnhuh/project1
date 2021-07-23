import re
import os
import sys

# Preprocess the text files for easier search
def preprocessing(text): 
    
    file = open(text, 'r')
    lines = file.readlines()
    
    outfile = open(text, 'w')
    for line in lines :
        # Remove all non-alphatic characters
        alpha = re.sub(r'[^A-Za-z]', ' ', line)
        res = ' '.join(alpha.split()).lower()
        outfile.write(alpha)
    outfile = open(text, "r")
    lines = outfile.readlines()
    
    outfile = open(text, 'w')
    for line in lines :
        # Convert tabs and newlines to only one whitespace
        whitespace = ' '.join(line.split())
        outfile.write(whitespace.lower())  # Change all upper case to lower case
    
    outfile.close()
    return 

preprocessing(sys.argv[1])
