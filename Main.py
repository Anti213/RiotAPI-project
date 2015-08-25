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
	#print(type(r))
	
	with open('itemList.json', 'r') as data_file:
		data = json.load(data_file)

	pprint(data)
	#pprint(r)
	
	
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