#!/usr/bin/python3
from RiotAPI import RiotAPI #import the class
import json
from pprint import pprint

def main():

	# get example data (matchReference.json)
	with open('matchReference.json', 'w') as data_file:
		match = json.load(data_file)
	
	# check if match is valid
	
	# make a dict with each champion
	
	# log each dict into its own csv file (we be using append)




if __name__ == "__main__":
	main()