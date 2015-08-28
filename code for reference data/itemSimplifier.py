#!/usr/bin/python3
from RiotAPI import RiotAPI #import the class
import json
from pprint import pprint

def main():

	# THIS CODE IS RUN ONE TIME ONLY
	# use match history from the LIST and access the data inside
	
	# For Items:
	# api = RiotAPI('3e888957-13a3-4ba2-901c-fae3e421d998')
	# r = api.get_match(1852538938)
	# r = api.get_itemList()
	
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
	with open('itemListTotal.json', 'r') as data_file:
		itemData = json.load(data_file)
	
	# get Ids of the items and put into an array
	nameIds = [nameId for nameId in itemData['data']]
	# get names of the items and put them into an array 
	itemNames = [itemData['data'][nameId]['name']
				 for nameId in itemData['data']]
	# get descriptions of the items and put them into an array
	itemDescriptions = [itemData['data'][nameId]['description']
						for nameId in itemData['data']]

	# link ID and names
	itemReference = dict(zip(nameIds, itemNames))
	# link ID and descriptions as a reference
	itemDescriptions = dict(zip(nameIds, itemDescriptions))

	pprint(itemReference)

	with open('itemListTotalReference.json', 'w') as outfile:
		json.dump(itemReference, outfile, indent=4)
	# sort the itemDescriptions
	# sortedItemIds = [nameId
	# 				for nameId in itemData['data']
	# 				if 'ability' or 'mana' or 'penetratin' in itemDescriptions[nameId].lower()]

	# sortedItemNames = [itemData['data'][nameId]['name']
	# 				   for nameId in sortedItemIds]

	# sortedItemDescriptions = [itemDescriptions[nameId]
	# 						  for nameId in itemData['data']
	# 						  if 'ability' or 'mana' or 'penetration' in itemDescriptions[nameId].lower()]
	
	# link sorted stuff properly
	#itemDescriptions2 = dict(zip(sortedItemIds, zip(sortedItemNames, sortedItemDescriptions)))
	#itemReference = dict(zip(sortedItemIds, sortedItemNames))

	# print to file for use in deleting unneeded entries
	# with open('itemReference.json', 'w') as outfile:
	#	json.dump(itemReference, outfile, indent=4)
	# print to file for information when deleting unneeded entires
	# with open('itemDescriptions.json', 'w') as outfile:
	#	json.dump(itemDescriptions, outfile, indent=4)
		
	# eliminate other values depending on phrases in the descriptions


	# better way to do list comprehensions?
	#nameIds = [nameId for nameId in itemData['data']]
	#itemNames = [itemData['data'][itemName]['name'] 
				 #for itemName in itemData['data']]
	#pprint(itemData['data']['3303']['name'])
	#itemNames = [itemName for itemName in nameIds]
	#pprint(nameIds)
	#pprint(itemNames)

	#dictionary = dict(zip(nameIds, itemNames))
	#pprint(dictionary)

	#with open('itemList.json', 'w') as outfile:
	#	json.dump(dictionary, outfile, indent=4)

	# convert dict data to JSON and write to .json
	#with open('data3.json', 'a') as outfile:
	#	json.dump(r, outfile, indent=4)


	#name = [names for names in itemData['data']['']]
	#for names in nameId:
		#n = int(names)
		#print(n)
		#print(nameId['data'][n])
		#print(type(int(names)))
	#itemNames = [[int(y) for y in nameId] for nameId in itemData['data'][nameId]]

	#pprint(nameId)



	# JUNK:
	# 
	# 	with open('unsortedItemData.json', 'w') as data_file:
	#	json.dump(r, data_file, indent=4)
		#itemList = dict(zip(nameId, itemData['data'][nameId]))
	#print(data['data'])
	#pprint(itemList)

# 	>>> keys = ['a', 'b', 'c']
# >>> values = [1, 2, 3]
# >>> dictionary = dict(zip(keys, values))
# >>> print dictionary

	#for ID, erum in data['data']['name']:
	#	print(ID + ": " + erum)
	#pprint(data)
	#pprint(r)
	#print(data['data']['name'])
	#print(data['data'].items())
	#pprint(data['data'])
	#x = data['data']['3723']
	#pprint(x)
	# use created reference data for now...
	# with open('data2.json', 'r') as data_file:
	# 	data = json.load(data_file)

	# pprint(data['participantIdentities'][10])

	# convert dict data to JSON and write to .json
	#with open('data3.json', 'a') as outfile:
	#	json.dump(r, outfile, indent=4)


	# testing to see if there is anything lost in conversion SUCCESS
	# with open('/home/lenneth/Documents/RiotAPI project/data.json', 'r') as data_file:
	# 	data_2 = json.load(data_file)

	# print(type(data_2))
	# if(r == data_2):
	# 	print('woo')
	# else:
	# 	print('ahh')
	
if __name__ == "__main__":
	main()