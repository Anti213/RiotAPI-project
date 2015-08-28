#!/usr/bin/python3
from RiotAPI import RiotAPI #import the class
import json
from pprint import pprint

def main():

	# THIS CODE IS RUN ONE TIME ONLY (#SAVETHESERVERS)
	
	# For Champions:
	#api = RiotAPI('3e888957-13a3-4ba2-901c-fae3e421d998')
	#r = api.get_championList()

	#with open('testChampion.json', 'w') as outfile:
	#	json.dump(r, outfile, indent=4)
	
	# --------------------------------------------------------

	with open('testChampion.json', 'r') as data_file:
		data = json.load(data_file)

	championIds = [data['data'][championName]['id'] 
				   for championName in data['data']]	
	championNames = [championName for championName in data['data']]
	championTitles = [data['data'][championName]['title'] 
				      for championName in data['data']]

	championReference = dict(zip(championIds, 
							 zip(championNames, championTitles)))
	
	with open('championReference.json', 'w') as outfile:
		json.dump(championReference, outfile, indent=4)

	#pprint(championReference)

	#pprint(championTitles)

	#pprint(data)

	#championIds = [championId['id'] for championId in data['champions']]
	#pprint(championIds)
	# write the data into a file so its not needed
	# to access the API all the time
	# with open('itemListTotal.json', 'w') as outfile:
	# 	json.dump(r, outfile, indent=4)

	# ------------------------------------
	# Processing: The goal is to partially simplify the JSON data
	# to figure out what to delete. Then, the completely simplified file
	# named 'itemReference.json'/'championReference.json'
	# /'matchReference.json' will be used in future code.


	# For Items:
	# with open('itemListTotal.json', 'r') as data_file:
	# 	itemData = json.load(data_file)
	
	# # get Ids of the items and put into an array
	# nameIds = [nameId for nameId in itemData['data']]
	# # get names of the items and put them into an array 
	# itemNames = [itemData['data'][nameId]['name']
	# 			 for nameId in itemData['data']]
	# # get descriptions of the items and put them into an array
	# itemDescriptions = [itemData['data'][nameId]['description']
	# 					for nameId in itemData['data']]

	# # link ID and names
	# itemReference = dict(zip(nameIds, itemNames))
	# # link ID and descriptions as a reference
	# itemDescriptions = dict(zip(nameIds, itemDescriptions))

	
if __name__ == "__main__":
	main()