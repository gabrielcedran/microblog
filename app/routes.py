from crypt import methods
from flask import flash, redirect, render_template, url_for
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember me {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)