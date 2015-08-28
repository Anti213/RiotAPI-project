#!/usr/bin/python3
from RiotAPI import RiotAPI #import the class
import json
from pprint import pprint
import matchParser as mParser

def main():

	# get example data (matchReference.json)
	with open('matchReference11.json', 'r') as data_file:
		data = json.load(data_file)

	# get reference data
	with open('itemReference.json', 'r') as data_file:
		itemRef = json.load(data_file)
	with open('championReference.json', 'r') as data_file:
		championRef = json.load(data_file)
	
	# check if match is valid
	if(mParser.matchValid(data, itemRef) == False):
		print('ahhh')
	else:
		# this writes to file as well
		mParser.makeParticipantDictionaries(data, itemRef, championRef)

		# with open('corki.json', 'r') as data_file:
		# 	monkey = json.load(data_file)
		# pprint(monkey)

if __name__ == "__main__":
	main()