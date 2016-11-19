

import urllib
import json 
import pprint
import requests

################################################
	#RETURNING A LIST OF ALL SUBJECTS IN A TERM
################################################

#to find all the subjects offered this quarter
#file1=urllib.urlopen('http://api.asg.northwestern.edu/subjects/?key=2EJqD5PCbVie7742&term='+Term+'')
#sublist=file1.read()
#parsed_json = json.loads(sublist)

#for element in parsed_json:
#	print element['symbol']

#########################################
	#SELECTING A SUBJECT FROM DROPDOWN
#########################################
SUBJECT=raw_input('Enter Subject: ')

#######################################################################
	#RUNNING THE API FOR THE SELECTED SUBJECT TO RETURN COURSES OFFERED
#######################################################################
params = {
  'key': '2EJqD5PCbVie7742',
  'term': 4640,
  'subject': SUBJECT
}
response = requests.get('http://api.asg.northwestern.edu/courses/', params=params)

########################################################################
	#PARSING THE API RESPONSE TO RETURN UNIQUE COURSE NUMBERS AS A LIST 
########################################################################
catalognumbers = set([x["catalog_num"] for x in response.json()])
catalognumbers = list(catalognumbers)]




