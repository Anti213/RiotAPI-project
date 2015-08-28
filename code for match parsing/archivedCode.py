	#for category in data['teams'][0]:
	#	print(category)
	#	
		# 2. LETS MAKE THE DICTIONARY NOW
	for participantId in participantIds:
		
		# definitions for compactness
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