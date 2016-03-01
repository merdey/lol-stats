'''
This project isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone
officially involved in producing or managing League of Legends. League of Legends and Riot Games are trademarks
or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.
'''


import requests


mapping_table = {
    # Champion
    'champions': '/api/lol/{region}/v1.2/champion',
    'champion': '/api/lol/{region}/v1.2/champion/{id}',

    # Champion Mastery
    'champion_mastery': '/championmastery/location/{platformId}/player/{playerId}/champion/{championId}',
    'champion_mastery_for_player': '/championmastery/location/{platformId}/player/{playerId}/champions',
    'champion_mastery_score': '/championmastery/location/{platformId}/player/{playerId}/score',
    'top_champions': '/championmastery/location/{platformId}/player/{playerId}/topchampions',

    # Game
    'current_game': '/observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}',
    'featured_games': '/observer-mode/rest/featured',
    'recent_game': '/api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent',

    # League
    'league_by_summoner_id': '/api/lol/{region}/v2.5/league/by-summoner/{summonerIds}',
    'league_entries_by_summoner_id': '/api/lol/{region}/v2.5/league/by-summoner/{summonerIds}/entry',
    'league_by_team_id': '/api/lol/{region}/v2.5/league/by-team/{teamIds}',
    'league_entries_by_team_id': '/api/lol/{region}/v2.5/league/by-team/{teamIds}/entry',
    'challenger_leagues': '/api/lol/{region}/v2.5/league/challenger',
    'master_leagues': '/api/lol/{region}/v2.5/league/master',

    # Static Data
    'champions_static': '/api/lol/static-data/{region}/v1.2/champion',
    'champion_static': '/api/lol/static-data/{region}/v1.2/champion/{id}',
    'items': '/api/lol/static-data/{region}/v1.2/item',
    'item': '/api/lol/static-data/{region}/v1.2/item/{id}',
    'language_strings': '/api/lol/static-data/{region}/v1.2/language-strings',
    'languages': '/api/lol/static-data/{region}/v1.2/languages',
    'map': '/api/lol/static-data/{region}/v1.2/map',
    'masteries': '/api/lol/static-data/{region}/v1.2/mastery',
    'mastery': '/api/lol/static-data/{region}/v1.2/mastery/{id}',
    'realm': ' /api/lol/static-data/{region}/v1.2/realm',
    'runes': '/api/lol/static-data/{region}/v1.2/rune',
    'rune': '/api/lol/static-data/{region}/v1.2/rune/{id}',
    'summoner_spells': '/api/lol/static-data/{region}/v1.2/summoner-spell',
    'summoner_spell': ' /api/lol/static-data/{region}/v1.2/summoner-spell/{id}',
    'versions': '/api/lol/static-data/{region}/v1.2/versions',

    # Status
    'shards': '/shards',
    'shards_by_region': '/shards/{region}',

    # Match/Match list
    'match': '/api/lol/{region}/v2.2/match/{matchId}',
    'match_list_by_summoner_id': '/api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}',

    # Stats
    'ranked_stats': '/api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/ranked',
    'stats_summary': '/api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/summary',

    # Summoner
    'summoner_by_name': '/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}',
    'summoner_by_id': '/api/lol/{region}/v1.4/summoner/{summonerIds}',
    'summoner_masteries_by_id': '/api/lol/{region}/v1.4/summoner/{summonerIds}/masteries',
    'summoner_name_by_id': '/api/lol/{region}/v1.4/summoner/{summonerIds}/name',
    'summoner_runes_by_id': '/api/lol/{region}/v1.4/summoner/{summonerIds}/runes',

    # Team
    'team_by_summoner_id': '/api/lol/{region}/v2.4/team/by-summoner/{summonerIds}',
    'team_by_team_id': '/api/lol/{region}/v2.4/team/by-summoner/{summonerIds}',
}


api_key = ''
class RiotApi:
    def __init__(self, api_key, default_region='na'):
        self.api_key = api_key
        self.auth_param = '?api_key=%s' % api_key
        self.default_region = default_region
        self.base_url = 'https://na.api.pvp.net'
        self.mapping_table = mapping_table

    def __getattr__(self, api_call):
        def call(self, **kwargs):
            if 'region' not in kwargs:
                kwargs['region'] = self.default_region
            path = self.mapping_table[api_call]
            path = path.format(**kwargs)
            url = self.base_url + path + self.auth_param

            response = requests.get(url)
            return response.json()

        if api_call not in self.mapping_table:
            raise AttributeError('Method "%s" Does Not Exist' % api_call)

        return call.__get__(self)


rapi = RiotApi(api_key)
res = rapi.summoner_by_name(summonerNames='xhatterz')
my_id = res['xhatterz']['id']

res = rapi.top_champions(playerId=my_id)
print(res)
