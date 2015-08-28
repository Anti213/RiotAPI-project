URL = {
	'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
	'itemBase': 'https://{proxy}.api.pvp.net/api/lol/static-data/{region}/{url}',
	'summoner_by_name': 'v{version}/summoner/by-name/{names}',
	'stats': 'v{version}/stats/by-summoner/{summonerId}/{gameTypes}',
	'match': 'v{version}/match/{matchId}',
	'itemList': 'v{version}/item',
	'championList': 'v{version}/champion'
}

API_VERSIONS = {
	'summoner': '1.4',
	'stats': '1.3',
	'match': '2.2',
	'itemList': '1.2',
	'championList': '1.2'
}

REGIONS = {
	'north_america': 'na'
}