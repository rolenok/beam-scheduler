from flask import render_template, flash, redirect, url_for
from app import app

from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user
from flask_login import login_required

@app.route('/')
@app.route('/index')
@login_required
def index():
	return render_template('public/index.html', title='Home', user=user)

@app.route('/public/LBNL')
@login_required
def LBNL():

	return render_template('public/LBNL.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	return render_template('public/login.html',title='Sign In', form=form)

@app.route('/public/schedule', methods=['GET'])
@login_required
	def schedule():
		if current_user.is_authenticated:
			return render_template('public/schedule.html', title='Main View')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('admin/integrator/schedule', methods=['GET','POST'])
@login_required
	def admin_schedule:
	if current_user.is_authenticated:
		return render_template('admin/integrator/schedule.html', title='Main View')