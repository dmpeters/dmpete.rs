import requests
from bottle import error, get, route, run, static_file, template 

# shit to consider:
#	- cache shit
#   - highlight.js (highlight syntax)


# routes
@route('/')
def index():
    return template('index')


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
run(reloader=True)
