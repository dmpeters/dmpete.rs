import requests
from collections import OrderedDict
from bottle import error, get, route, run, static_file, template, debug

# shit to consider:
#	- cache shit
#   - highlight.js (highlight syntax)

# settings
GITHUB_USERNAME = 'dmpeters'

# routes
@route('/')
def index():
    # github
    me = {}
    github = requests.get('https://api.github.com/users/'+GITHUB_USERNAME)
    response = github.json()

    fields = ['blog',
              'login',
              'name',
              'company',
              'hireable',
              'public_repos',
              'public_gists'
             ]

    for key in fields:
        if key in response:
            me[key] = response[key]

    obj = OrderedDict(sorted(me.items()))

    json = template('index', obj=obj)
    return json

# static
@get('/<file:re:.*\.js>')
def js(file):
    return static_file(file, root='static/js')

@get('/<file:re:.*\.css>')
def css(file):
    return static_file(file, root='static/css')

@get('/<file:re:.*\.(jpg|png|gif|ico)>')
def imgs(file):
    return static_file(file, root='static/img')


# error
@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

@error(500)
def mistake500(code):
    return 'GFY!'


# run
debug(True)
run(reloader=True)
