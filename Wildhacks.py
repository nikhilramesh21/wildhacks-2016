

import urllib
import json 
import pprint
import requests

################################################
	#RETURNING A LIST OF ALL SUBJECTS IN A TERM
################################################

#to find all the subjects offered this quarter
params = {
  'key': '*REQUEST API KEY HERE: http://developer.asg.northwestern.edu/*',
  'term': 4640,
}
response = requests.get('http://api.asg.northwestern.edu/subjects/', params=params)
sublist = set([x["symbol"] for x in response.json()])
sublist = list(sublist)



####################################################################################
	#RUNNING THE API TO GENERATE A LIST OF ALL COURSES OFFERED IN A TERM BY SUBJECT
####################################################################################
courses = {}
for subject in sublist:
	courses[subject] = []
	params1 = {
	  'key': '*REQUEST API KEY HERE: http://developer.asg.northwestern.edu/*',
	  'term': 4640,
	  'subject': subject
	}
	response1 = requests.get('http://api.asg.northwestern.edu/courses/', params=params1)
	
	catalognumbers = set([x["catalog_num"] for x in response1.json()])
	courses[subject] = list(catalognumbers)



