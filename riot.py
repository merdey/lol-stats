import requests

from api_mappings import api_mappings

class RiotApi:
    def __init__(self, api_key, region='na'):
        self.api_key = api_key
        self.auth_param = '?api_key=%s' % api_key
        self.region = region
        self.base_url = 'https://na.api.pvp.net'
        self.api_mappings = api_mappings

    def __getattr__(self, api_call):
        def call(self, **kwargs):
            if 'region' not in kwargs:
                kwargs['region'] = self.region
            path = self.api_mappings[api_call]
            path = path.format(**kwargs)
            url = self.base_url + path + self.auth_param

            response = requests.get(url)
            return response.json()

        if api_call not in self.api_mappings:
            raise AttributeError('Method "%s" Does Not Exist' % api_call)

        return call.__get__(self)
    

def get_riot_client():
    api_key = '3e006de3-a31d-468b-8eb9-130307886d0b'
    riot = RiotApi(api_key)
    return riot