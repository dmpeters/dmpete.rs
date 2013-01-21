import requests

import .settings
import .models


class GetRescource():

    def __init__(self):
        ''' Docs goe here...
        '''
        model = rescource.model
        url = rescource.url
        name - rescource.name

        obj = {}
        rescource = requests.get(url+name)
        rescource_dict = rescource.json()

        for key in model:
            if key in rescource_dict:
                obj[key] = rescource_dict[key]

        return obj


class PutRescource(self, rescource):
    pass


class PostRescource(self, rescource):
    pass
