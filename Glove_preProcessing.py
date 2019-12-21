# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:12:06 2019

@author: Koustubh
reference-https://medium.com/@japneet121/word-vectorization-using-glove-76919685ee0b
"""

import os, sys, nltk, re
from __future__ import division
from sklearn.cluster import KMeans
from numbers import Number
from pandas import DataFrame
import sys, codecs, numpy
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
#from glove import Corpus, Glove

#os.chdir('Desktop\SDM2\project')
path = "corpus"
dirs = os.listdir(path)
alldata=[]
finaldata=[]
temp=[]
for file in dirs:
	path_to_file=path+'/'
	file_name = file
	path_to_file += file_name
	with open(path_to_file, 'r', encoding = 'latin1') as f:
		mylist = f.read()
		sent_tokenize_list = nltk.sent_tokenize(mylist)
		for i in sent_tokenize_list:
			sent = i.lower()
			sent = re.sub('[^A-Za-z0-9]+', ' ', sent)
			temp.append(sent)
		alldata.append(temp)
		

with open('ALL_Corpus1.txt', 'a',encoding='utf8') as f:
    for item in alldata:
        f.write("%s " % item)	

ps = PorterStemmer()
for a in alldata:
	ps.stem(a)
	alldata=' '.join(alldata)
	
	stop_words = set(stopwords.words('english')) 
	  
	word_tokens = word_tokenize(alldata)
	filtered_sentence = [w.lower() for w in word_tokens if not w in stop_words and w.isalpha()] 
	filtered_sentence=' '.join(filtered_sentence)
	finaldata=finaldata.append(filtered_sentence)

new_lines=[] 
for line in finaldata: new_lines=line.split('') #new lines has the new format 
finaldata=new_lines

print(finaldata)