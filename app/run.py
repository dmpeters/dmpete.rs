import requests
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# settings
DEBUG = True
SECRET_KEY = 'dmpe1rft=r-llc_!t9$zc!ype6u-k_*e+#3718-r6mi&2f@5&3+6ote.rs'
GITHUB_USERNAME = 'dmpeters'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    obj = requests.get('https://api.github.com/users/'+GITHUB_USERNAME)
    return render_template('index.html', user=obj.json())

@app.route("/gists")
def gists():
    obj = requests.get('https://api.github.com/users/gists/'+GITHUB_USERNAME)
    return render_template('gists.html', gists=obj.json())

if __name__ == "__main__":
    app.run()
