from flask import render_template
from app import app


@app.route('/')
@app.route('/index')


def index():
    user = {'username':'ameer'}
    posts = [
        {
        'author': {
            'username' : 'john'
            },
            'body': 'Beautiful day in portland!'
        },
        {
        'author': {
            'username' : 'susan'
        },
            'body': 'Ah crap'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)