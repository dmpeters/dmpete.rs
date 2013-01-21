import requests

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

# flask apps to consider:
#   - flask-sqlalchemy > orm
#   - flask-peewee > orm
#   - flask-cache
#   - flask-celery > tasks (get new data & flush cache)
#   - forzen-flask > freeze into static site?
#   - flask-lesscss > less
#   - flask-testing
#   - flask-heroku


# settings
GITHUB_USERNAME = 'dmpeters'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd'
app.config['DEBUG'] = True

toolbar = DebugToolbarExtension(app)


# routes
@app.route("/")
def index():
    me = {}

    obj = requests.get('https://api.github.com/users/'+GITHUB_USERNAME)
    obj_dict = obj.json()

    fields = ['bio',
              'hireable',
              'id',
              'blog',
              'public_repos',
              'company',
              'public_gists',
              'name',
              'login'
              ]

    for key in fields:
        if key in obj_dict:
            me[key] = obj_dict[key]

    return render_template('index.html', user=me)


@app.route("/gists")
def gists():
    obj = requests.get('https://api.github.com/users/gists/'+GITHUB_USERNAME)
    return render_template('gists.html', gists=obj.json())


if __name__ == "__main__":
    app.run()
