#!/usr/bin/env python
"""
Created on Thur May 11 01:52:00 2017
@author: Dr. Briefs

@Notes: reads pubmed_index.csv, extracts and creates list for keywords & cited authors, and saves new dataframe to csv for conveniently formatted parsing
"""

import pandas as pd
import os
import rake
df = pd.read_csv('pubmed_index.csv')

'''
#text = str("Quantum-optical properties of polariton waves.")
text = str(df.title[df.PubMedID==10000001][0])
print text
print rake.extract(text)
#print len(rake.extract(text))
'''

for row in range( 0, len(df) ):
	# PubMedID
	PubMedID = df.loc[row,'PubMedID']
	
	# authors
	authors = df.loc[row,'authors']
	
	# pubmed_url
	pubmed_url = df.loc[row,'pubmed_url']
	
	# extract keywords from title and place them in a list
	title = df.loc[row,'title']
	keywords = rake.extract(title) 	# use rake keyword identifier to extract keyword list
	
	# extract cited authors from citation and place them in a list
	citation = df.loc[row,'citation']
	for i in range(0,len(citation)): 	# locate where citation author names end in string
		if citation[i] == '(':	# dates references begin with '(', so use it to define end of substring			
			break	# break 'for loop' and use last value from loop counter to truncate 'citation' string
	substring = citation[0:i]	# create substring
	cited_authors = substring.split(", ")	# split string into list, using ", " as delimiters
	
	# create tuple containing formatted pubmed index entry
	pubmed_index_formatted = [(PubMedID, title, authors, pubmed_url, cited_authors, keywords)] 
	
	# create dataframe containing formatted index entry
	df_formatted = pd.DataFrame(pubmed_index_formatted, columns = ['PubMedID','title','authors','pubmed_url','cited_authors','keywords'])
	
	# if file does not exist, write header
	if not os.path.isfile('pubmed_index_formatted.csv'):
		print 'Formatting id_no #',PubMedID,'...','\n'
		df_formatted.to_csv('pubmed_index_formatted.csv',header ='column_names')
	elif any(pd.read_csv('pubmed_index_formatted.csv')['PubMedID']==PubMedID):
		print 'repeat no:',PubMedID,'\n'
	else: # else it doesn't exists, so append without writing the header
		print 'Formatting index #',PubMedID,'...','\n'
		df_formatted.to_csv('pubmed_index_formatted.csv',mode = 'a', header=False)
	

