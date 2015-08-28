import requests
import RiotConsts as Consts

class RiotAPI(object):

	# init is like a constructor
	# the 'region=Consts' thing means that if not specified, the default will be 'north america'
	def __init__(self, api_key, region=Consts.REGIONS['north_america']):
		self.api_key = api_key
		self.region  = region

	# NOTE ON PARAMS
	# For the url:
	# https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/anti213?api_key=3e888957-13a3-4ba2-901c-fae3e421d998
	# The 'params' is all the stuff AFTER the '?' character... we have an api_key and an = with the key following

	# most basic request
	def _request(self, api_url, params={}):
		args = {'api_key': self.api_key}
		for key, value in params.items():
			if key not in args:
				args[key] = value
		response = requests.get(
			Consts.URL['base'].format(
				proxy  = self.region,
				region = self.region,
				url    = api_url
				), # format command lets us replace the bracketed stuff earlier
			params = args
			)
		# parses the string into a 'dictionary'
		#print (response.url)
		return response.json()

	# item request
	def _requestItems(self, api_url, params={}):
		args = {'api_key': self.api_key}
		for key, value in params.items():
			if key not in args:
				args[key] = value
		response = requests.get(
			Consts.URL['itemBase'].format(
				proxy  = self.region,
				region = self.region,
				url    = api_url
				), # format command lets us replace the bracketed stuff earlier
			params = args
			)
		# parses the string into a 'dictionary'
		#print (response.url)
		return response.json()


	def get_summoner_by_name(self, name):
		api_url = Consts.URL['summoner_by_name'].format(
			version = Consts.API_VERSIONS['summoner'],
			names = name
		)
		return self._request(api_url)

	def get_stats(self, id, gameType):
		api_url = Consts.URL['stats'].format(
			version = Consts.API_VERSIONS['stats'],
			summonerId = id,
			gameTypes = gameType
		)
		return self._request(api_url)

	def get_match(self, id):
		api_url = Consts.URL['match'].format(
			version = Consts.API_VERSIONS['match'],
			matchId = id
		)
		return self._request(api_url)

	def get_itemList(self):
		api_url = Consts.URL['itemList'].format(
			version = Consts.API_VERSIONS['itemList']	
		)
		return self._requestItems(api_url)

	def get_championList(self):
		api_url = Consts.URL['championList'].format(
			version = Consts.API_VERSIONS['championList']
		)
		return self._requestItems(api_url)
