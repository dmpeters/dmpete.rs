import requests

from flask import Flask, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension


# flask apps to consider:
#   - flask-cache
#   - flask-celery > tasks (get new data & flush cache)
#   - flask-lesscss > less
#   - flask-testing
#   - highlight.js (highlight syntax)


# settings
GITHUB_USERNAME = 'dmpeters'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd'
app.config['DEBUG'] = True

toolbar = DebugToolbarExtension(app)

app = Flask(__name__)


# routes
@app.route("/")
def imdex():
    return render_template('index.html')


@app.route("/github")
def github():
    # obj that gets passed to my template
    obj = {}

    # github
    me = {}
    github = requests.get('https://api.github.com/users/'+GITHUB_USERNAME)
    github_response = github.json()

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
        if key in github_response:
            me[key] = github_response[key]

    # gists
    gists = []
    gist_objs = requests.get('https://api.github.com/users/' + GITHUB_USERNAME + '/gists')
    gist_response = gist_objs.json()

    fields = ['id',
              'html_url',
              'created_at',
              'updated_at',
              'description',
              'comments',
              ]

    for gist in gist_response:
        gists_dict = {}

        for key in fields:
            if key in gist:
                gists_dict[key] = gist[key]
        gists.append(gists_dict)

    obj.update({'github': me})
    obj.update({'gists': gists})

    if len(me) < 1:
        return jsonify(obj=github['message'])
    else:
        return jsonify(obj=obj)


@app.route("/linkedin")
def linkedin():
    return jsonify(obj='obj')


@app.route("/twitter")
def twitter():
    return jsonify(obj='obj')


if __name__ == "__main__":
    app.run()
