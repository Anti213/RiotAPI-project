#!/usr/bin/python3
from RiotAPI import RiotAPI #import the class
import json
from pprint import pprint

def main():

	# # use the JSON match history file and load it into a LIST
	# with open('/home/lenneth/Documents/RiotAPI project/'
	# 	 	  'json data/5.11/RANKED_SOLO/NA.json', 'r') as data_file:
	# 	data = json.load(data_file)


	# use match history from the LIST and access the data inside
	api = RiotAPI('3e888957-13a3-4ba2-901c-fae3e421d998')
	#r = api.get_match(1852538938)
	#r = api.get_itemList()
	#print(r)
	


	#for nameId in itemData['data']:
	#	print(nameId)
	

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