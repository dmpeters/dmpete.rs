import requests
from bottle import error, route, run, static_file, template 

# shit to consider:
#	- cache shit
#   - highlight.js (highlight syntax)


# routes
@route("/")
def index():
    return template('index')


@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


@error(500)
def mistake500(code):
    return 'GFY!'


run(reloader=True)
