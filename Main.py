#!/usr/bin/python3
from RiotAPI import RiotAPI #import the class
import json
from pprint import pprint
import matchParser as mParser

def main():

	# get data
	api = RiotAPI('3e888957-13a3-4ba2-901c-fae3e421d998')
	data = api.get_match(1900729148)

	# write the data into a file so its not needed
	# to access the API all the time
	#with open('matchReference14.json', 'w') as outfile:
		#json.dump(r, outfile, indent=4)
	# get reference data
	with open('itemReference.json', 'r') as data_file:
		itemRef = json.load(data_file)
	with open('championReference.json', 'r') as data_file:
		championRef = json.load(data_file)
	
	# check if match is valid or not
	if(mParser.matchValid(data, itemRef) == False):
		print('ahhh')
	else:
		# this writes to file as well
		mParser.makeParticipantDictionaries(data, itemRef, championRef)

	#pprint(data['participants'][0]['participantId'])
		# with open('corki.json', 'r') as data_file:
		# 	monkey = json.load(data_file)
		# pprint(monkey)

if __name__ == "__main__":
	main()