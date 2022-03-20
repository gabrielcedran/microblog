from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'donbob'}
    posts = [
        {
            'author': { 'username': 'Don'},
            'body': 'My first post here, nice to meet you'
        },
        {
            'author': { 'username': 'Bob'},
            'body': 'I cannot wait for summer'
        },
        {
            'author': { 'username': 'Mary'},
            'body': 'Do you belive in E.T\'s?'
        }
    ]
    return render_template('index.html', title='Home Page', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)