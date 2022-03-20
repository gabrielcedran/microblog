from crypt import methods
from flask import flash, redirect, render_template, url_for
from flask_login import logout_user
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid user or password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
