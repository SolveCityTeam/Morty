#!/usr/bin/env python3
"""
Created on Fri Apr 28 11:30:56 2017
@author: Dr. Briefs

@Dependencies: Requires 'PubMedLookup' Python module from https://github.com/mfcovington/pubmed-lookup
"""

from pubmed_lookup import PubMedLookup
from pubmed_lookup import Publication
import pandas as pd
import os

def search(PubMedID):
	# Retrieve a PubMed record:
	# NCBI will contact user by email if excessive queries are detected
	"""
	Retrieve a PubMed record using its PubMed ID or PubMed URL.
	(e.g., '22331878' or 'http://www.ncbi.nlm.nih.gov/pubmed/22331878')
	"""
	email = ''
	#url = 'http://www.ncbi.nlm.nih.gov/pubmed/22331878'
	#lookup = PubMedLookup(url, email)
	#print(type(PubMedID))
	lookup = PubMedLookup(PubMedID,email)

	# Create a Publication object:
	publication = Publication(lookup)    # Use 'resolve_doi=False' to keep DOI URL

	# Access the Publication object's attributes:
	tupleoutput = [(
		PubMedID,
		publication.title,
		publication.authors,
		publication.journal,
		publication.year,
		publication.month,
		publication.day,
		#publication.url,	# doesn't seem to work w/ dataframe
		publication.pubmed_url,
		publication.cite(),
		publication.cite_mini(),
		repr(publication.abstract),
		0,
	)]
	
	return tupleoutput
	
#print(search('','ewchehab@rice.edu'))
#print(search(22331878))

for id_no in range(10021315, 28470030):
	#print(tuple(id_no))
#	df = pd.DataFrame(search(id_no), columns=['PubMedID','title','authors','journal','year','month','day','url','pubmed_url','citation','mini_citation','abstract','pagerank'])
	df = pd.DataFrame(search(id_no), columns=['PubMedID','title','authors','journal','year','month','day','pubmed_url','citation','mini_citation','abstract','pagerank'])

	# Save scraped index entry to csv
	if not os.path.isfile('pubmed_index.csv'):	# if file does not exist write header 
		print('Parsing id_no #',id_no,'...'),
		df.to_csv('pubmed_index.csv',header ='column_names')
	elif any(pd.read_csv('pubmed_index.csv')['PubMedID']==id_no):	# if entry already exists, ignore
		print('repeat no:',id_no)
	else:	# else it doesn't exists, so append without writing the header
		print('Parsing id_no #',id_no,'...'),
		df.to_csv('pubmed_index.csv',mode = 'a',header=False)


