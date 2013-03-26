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

    # github
    me = {}
    github = requests.get('https://api.github.com/users/'+GITHUB_USERNAME)
    github_dict = github.json()

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
        if key in github_dict:
            me[key] = github_dict[key]

    # gists
    gists_dict = {}
    gists = []
    gist_objs = requests.get('https://api.github.com/users/'+ GITHUB_USERNAME +'/gists')
    gist_dict = gist_objs.json()

    fields = ['id',
              'html_url',
              'files',
              'created_at',
              'updated_at',
              'description',
              'comments',
              ]

    for gist in gist_dict:
        for key in fields:
            if key in gist:
                gists_dict[key] = gist[key]
        gists.append(gists_dict)

    import pdb; pdb.set_trace()

    return render_template('gists.html', gists=gists)
    return render_template('index.html', user=me)


if __name__ == "__main__":
    app.run()
