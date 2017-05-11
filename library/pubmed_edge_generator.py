#!/usr/bin/env python
"""
Created on Thur May 11 07:16:00 2017
@author: Dr. Briefs

@Notes: reads pubmed_index_formatted.csv, and generates pubmed_edges.csv
	Script cannot update existing edge files; delete any existing pubmed_edges.csv files before running script
"""

import pandas as pd
import os
import rake
df = pd.read_csv('pubmed_index_formatted.csv')


for row in range( 0, len(df) ):

	# PubMedID
	sourcenode = df.loc[row,'PubMedID']
	print 'Cross referencing edges for source node,',sourcenode,'...','\t'
	
	'''
	# authors
	authors = df.loc[row,'authors']
	
	# pubmed_url
	pubmed_url = df.loc[row,'pubmed_url']
	
	# extract keywords from title and place them in a list
	title = df.loc[row,'title']
	keywords = rake.extract(title) 	# use rake keyword identifier to extract keyword list
	'''
	
	# for number of cited authors listed, cross reference all articles containing said author(s) and save as edge entry
	cited_authors = df.loc[row,'cited_authors'].split(", ")	# create list of cited authors for entry in current row
	for i in range(0,len(cited_authors)): 	# for entire list of cited authors, i
		for j in range(0,len(df)): # for entire lenth of dataframe,
			authors = df.loc[j,'authors'].split(", ") # create list for authors mentioned in entry, j
			for k in range(0,len(authors)):	# for each author, k, mentioned in entry, j,
				if cited_authors[i] == authors[k]:	# if author, k, is one of the cited authors, i, then:
					targetnode = df.loc[j,'PubMedID']	# PubMedID of article, j, is target node
					
					if sourcenode != targetnode:	# if sourcenode not equal to targetnode
						edge = [(sourcenode,targetnode)]	# record as edge in tuple
					
						# create dataframe containing edge entry
						df_edge = pd.DataFrame(edge, columns = ['sourcenode','targetnode'])
					
						# save edge entry to csv file
						if not os.path.isfile('pubmed_edges.csv'):	# if file does not exist, write header
							print 'Saving edge:',sourcenode,targetnode,'...','\n'
							df_edge.to_csv('pubmed_edges.csv',header ='column_names')
						#elif any(pd.read_csv('pubmed_edges.csv')['sourcenode']==sourcenode) :
						#	print 'repeat no:',PubMedID,'\n'
						else: # else it doesn't exists, so append without writing the header
							print 'Saving edge',sourcenode,targetnode,'...','\n'
							df_edge.to_csv('pubmed_edges.csv',mode = 'a', header=False)


