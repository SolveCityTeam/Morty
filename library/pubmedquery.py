#!/usr/bin/env python3
"""
Created on Fri Apr 28 11:30:56 2017
@author: Dr. Briefs

@Notes: uses PubMedLookup Python module obtained from here:
https://github.com/mfcovington/pubmed-lookup
"""


from pubmed_lookup import PubMedLookup
from pubmed_lookup import Publication

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
	lookup = PubMedLookup(PubMedID,email)

	# Create a Publication object:
	publication = Publication(lookup)    # Use 'resolve_doi=False' to keep DOI URL

	# Access the Publication object's attributes:
	tupleoutput = (
	"""
	TITLE:\n{title}\n
	AUTHORS:\n{authors}\n
	JOURNAL:\n{journal}\n
	YEAR:\n{year}\n
	MONTH:\n{month}\n
	DAY:\n{day}\n
	URL:\n{url}\n
	PUBMED:\n{pubmed}\n
	CITATION:\n{citation}\n
	MINICITATION:\n{mini_citation}\n
	ABSTRACT:\n{abstract}\n
	"""
	.format(**{
	  'title': publication.title,
	  'authors': publication.authors,
	  'journal': publication.journal,
	  'year': publication.year,
	  'month': publication.month,
	  'day': publication.day,
	  'url': publication.url,
	  'pubmed': publication.pubmed_url,
	  'citation': publication.cite(),
	  'mini_citation': publication.cite_mini(),
	  'abstract': repr(publication.abstract),
	}))
	
	return tupleoutput
	
#print(search('','ewchehab@rice.edu'))
print(search(22331878))

