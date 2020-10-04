from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'Duncan'}
	return render_template('public/index.html', title='Home', user=user)


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('public/login.html',title='Sign In', form=form)

