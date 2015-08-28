import json
from pprint import pprint
import os

def matchValid(data, itemRef):
	#print(type(data['matchVersion']))
	if '5.11' in data['matchVersion'] and checkItems(data, itemRef):
		#print('5.11')
		return True
	elif '5.14' in data['matchVersion'] and checkItems(data, itemRef):
		#print('5.14')
		return True
	else:
		return False

# boolean to check if there are any ap items in the game
def checkItems(data, itemRef):
	
	# store all item data from the match
	itemList = [participant['stats'][datum] 
			 for participant in data['participants']
			 for datum in participant['stats'] if 'item' in datum]

	# see if there are any AP items. if there is, return True
	for item in itemList:
		if str(item) in itemRef:
			return True
	return False

# check validity of 

# make a dictionary containing the data of 
def makeParticipantDictionaries(data, itemRef, championRef):

	# 1. If there is an ap item, link it to its player
	
	# definitions
	participantIds = []
	csvHeader = []

	# reference stuff
	itemIds = ['item0', 'item1', 'item2', 
			   'item3', 'item4', 'item5', 'item6']
	
	# lvl 1
	categories = ['teams', 'matchVersion', 'queueType', 
				  'matchCreation', 'region', 'matchDuration']
	# cut teams, participants

	# lvl 2
	# 'participants' exceptions
	p_Exceptions = ['masteries', 'participantId', 'runes', 'timeline']				  
	# lvl 3
	teamsExceptions = ['dominionVictoryScore', 'vilemawKills']
	#'timeline' exceptions
	t_Exceptions = ['xpDiffPerMinDeltas', 'damageTakenDiffPerMinDeltas',
					'csDiffPerMinDeltas']

	# LINKAGE
	for participant in data['participants']:
		for itemId in itemIds:
			if(str(participant['stats'][itemId]) in itemRef):
				participantIds.append(participant['participantId'])
				break


	# 2. LETS MAKE THE DICTIONARY NOW
	for participantId in participantIds:
		
		# definitions for compactness
		count = 0
		championDict = dict()
		teamId = data['participants'][participantId]['teamId']
		championName = championRef[str(data['participants']
								   [participantId]['championId'])]
		# general data/team data
		# lvl 1 champion key
		championDict['championName'] = championName[0]
		championDict['championTitle'] = championName[1]
		
		# lvl 1 easy to clone data
		for category in categories:
			championDict[category] = data[category]
		
		# lvl 1 make sure that you get the team data that you want
		if(teamId == 100):
			championDict['teams'] = data['teams'][0]
		elif(teamId == 200):
			championDict['teams'] = data['teams'][1]
		
		# lvl 3 make sure to only get the specific data that you want
		championDict['participants'] = dict()
		for p_Categories in data['participants'][participantId]:
			if p_Categories not in p_Exceptions:
				championDict['participants'][p_Categories] = data['participants'][participantId][p_Categories]
		
		championDict['participants']['timeline'] = dict()
		for t_Categories in data['participants'][participantId]['timeline']:
			if t_Categories not in t_Exceptions:
				championDict['participants']['timeline'][t_Categories] = data['participants'][participantId]['timeline'][t_Categories]
		


		# writing to file
		fileName = championName[0].lower() + '.json'
		with open(fileName, 'a') as outfile:
			if(os.stat(fileName).st_size == 0):
				outfile.write('[\n')
				print(fileName + ' WAS EMPTY')
			else:
				print(fileName + ' is OCCUPIEDD')
				count = 1

		if(count == 1):
			with open(fileName, 'rb+') as filehandle:
			    filehandle.seek(-1, os.SEEK_END)
			    filehandle.truncate()
			    filehandle.seek(-1, os.SEEK_END)
			    filehandle.truncate()
			with open(fileName, 'a') as outfile:
				outfile.write(',\n')
				json.dump(championDict, outfile, indent=4)
				outfile.write('\n]')
		else: 		
			with open(fileName, 'a') as outfile:
				json.dump(championDict, outfile, indent=4)
				outfile.write('\n]')

		# # validity of file



		# with open(filename, 'rb+') as filehandle:
		#     filehandle.seek(-1, os.SEEK_END)
		#     filehandle.truncate()

	return True

def makeGeneralDictionary(data):
	return True