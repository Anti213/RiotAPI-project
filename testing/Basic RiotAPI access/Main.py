from RiotAPI import RiotAPI #import the class
from pprint import pprint

def main():
	api = RiotAPI('3e888957-13a3-4ba2-901c-fae3e421d998')
	r = api.get_summoner_by_name('sadmilk')
	#print(r['anti213']['id'])
	r1 = api.get_stats(r['sadmilk']['id'], 'ranked')
	pprint(r1)

if __name__ == "__main__":
	main()

