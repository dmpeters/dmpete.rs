import requests
import redis


# settings
GITHUB_USERNAME = 'dmpeters'


def github():
    me = {}
    github = requests.get('https://api.github.com/users/'+GITHUB_USERNAME)
    response = github.json()
    fields = ['company', 'hireable', 'name', 'public_gists', 'public_repos']
    for key in fields:
        if key in response:
            me[key] = response[key]

    if not response:
        return {'github':'no es bueno!'}
    else:
        return {'github': me}

def gists():
    # gists
    gists = []
    gist = requests.get('https://api.github.com/users/' + GITHUB_USERNAME + '/gists')
    response = gist.json()
    fields = ['id', 'html_url', 'created_at', 'updated_at', 'description', 'comments']

    for gist in response:
        gists_dict = {}

        for key in fields:
            if key in gist:
                gists_dict[key] = gist[key]
        gists.append(gists_dict)

    if not response:
        return {'github':'no es bueno!'}
    else:
        return {'gists': gists}
