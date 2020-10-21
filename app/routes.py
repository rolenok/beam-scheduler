from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from app.models import User, Request
from flask_login import current_user, login_user, logout_user
from flask_login import login_required

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = {'username' : 'Duncan'}
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

@app.route('/requestForm', methods=['GET','POST'])
def requestForm():
	pushRequest()
	return render_template('request.html')


@app.route('/pushRequest',methods=['GET','POST'])
def pushRequest():
	try:
		facility = request.form['facility']
		beam = request.form['beam']
		beamSize = request.form['beam_size']
		ion = request.form['ion']
		energy = request.form['energy']
		fluence = request.form['fluence']
		flux = request.form['flux']
		start_date = request.form['start_date']
		end_date = request.form['end_date']
		hours = request.form['hours_req']

		tR = Request(facility=facility,beam=beam,beam_size=beamSize,ion=ion,energy=energy,
					 fluence=fluence,flux=flux,scheduled_start=start_date,scheduled_end=end_date,
					 hours=hours)
		tR.create_request()

	except Exception as e:
		return(str(e))

	return render_template('dbOutput.html',facility=tR.facility,beam=tR.beam,beam_size=tR.beam_size,
						   						   ion=tR.ion,energy=tR.energy,fluence=tR.fluence,flux=tR.flux,
												   start_date=tR.scheduled_start,end_date=tR.scheduled_end,
												   hours_req=tR.hours, data_info=tR.__repr__(),entry=tR)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
