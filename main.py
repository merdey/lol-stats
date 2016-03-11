'''
This project isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone
officially involved in producing or managing League of Legends. League of Legends and Riot Games are trademarks
or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.
'''

from collections import defaultdict

from riot import get_riot_client


if __name__ == '__main__':
    riot_client = get_riot_client()
    res = riot_client.summoner_by_name(summonerNames='xhatterz')

    my_id = res['xhatterz']['id']

    roles = defaultdict(int)
    champions = defaultdict(int)

    matches = riot_client.match_list_by_summoner_id(summonerId=my_id)['matches']
    for match in matches:
        roles[match['role']] += 1
        champions[match['champion']] += 1

    print(roles)
    print(champions)
