import re
import os
import sys
import pandas as pd
import nltk
import glob
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfTransformer
import math

# 3 given keywords
query_terms = [sys.argv[1], sys.argv[2], sys.argv[3]]

for file in matched_file:
    file = open(file, 'r').readlines()[0]
    words = word_tokenize(file)
    for word in words:
        if word not in terms :
            terms.append(porterStemmer.stem(word))

# For each document, store how many times stemmed words appear in a dictionary
term_counts = []
for file in matched_file:
    file = open(file, 'r').readlines()[0]
    wordDict1 = {}
    for term in terms :
        wordDict1[term] = 0
    term_count = []
    words = word_tokenize(file)
    for word in words:
        stemword = porterStemmer.stem(word)
        if stemword in wordDict1 :
            wordDict1[stemword] += 1 
    for key, value in wordDict1.items():
        term_count.append(value)
    term_counts.append(term_count)

    
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(term_counts)
transformer.idf_
doc_tfidf = tfidf.toarray()
    
query_vector = []
wordDict2 = {}
for term in terms :
    wordDict2[term] = 0
for term in query_terms:
    stemword = porterStemmer.stem(term)
    if stemword in wordDict2:
        wordDict2[stemword] += 1
for key, value in wordDict2.items():
    query_vector.append(value)

q_unit = [x/math.sqrt(len(query_terms)) for x in query_vector]

from numpy import dot
from numpy.linalg import norm

def cosine_sim(v1, v2):
    return dot(v1, v2)/(norm(v1)*norm(v2))

sims = [cosine_sim(q_unit, doc_tfidf[d_id]) for d_id in range(doc_tfidf.shape[0])]

data = {'documentID':matched_id, 'score':sims}
df = pd.DataFrame(data)
partb5 = df.sort_values(by='score', ascending=False)
partb5
