#!/usr/bin/python3
from RiotAPI import RiotAPI #import the class
import json
from pprint import pprint
import datetime
import matchSorter as mSort

def main():

	# THIS CODE IS RUN ONE TIME ONLY

	api = RiotAPI('3e888957-13a3-4ba2-901c-fae3e421d998')
	r = api.get_match(1900729148)
	#r = api.get_itemList()

	# write the data into a file so its not needed
	# to access the API all the time
	with open('matchReference14.json', 'w') as outfile:
		json.dump(r, outfile, indent=4)
	#----------------------------------------------------------
	
	#with open('matchReference.json', 'r') as data_file:
	#	data = json.load(data_file)
	#	data_file.close()
	#with open('matchLvl1.json', 'r') as data_file:
	#	matchLvl1 = json.load(data_file)
	#	data_file.close()
	#categoriesLvl1 = [categories for categories in data]
	#test = [categories for categories in data]
	#pprint(teams)

	#with open('matchTest.json', 'w') as outfile:
	#	json.dump(sortedLvl1, outfile, indent=4)
	#pprint(categoriesLvl1)
	#timestamp = 1433976950634
	#date = datetime.datetime.fromtimestamp(timestamp/1e3)
	
	#print(type(date.time()))

if __name__ == "__main__":
	main()