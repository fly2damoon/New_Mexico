from flask import render_template, flash, redirect, \
					session, url_for, request, g
from flask.ext.login import login_user, logout_user, \
							current_user, login_required
from src import app, db, lm
from .forms import LoginForm
from models.user import User, Team, Kid
from config import ITEMS_PER_PAGE

@app.route('/')
def index():
	"""Page - Landing Page. Do not need to be logged in"""
	loginform = LoginForm()
	return render_template('index.html', title="Welcome to New Mexico Missions", loginform=loginform)

@app.route('/lwrc/')
def lwrc():
	"""Page - Description of Living Water Retreat Center
	Introduce Missionary Sunny and Heave."""
	loginform = LoginForm()
	return render_template('lwrc.html', title="Living Water Retreat Center", \
							loginform=loginform)

@app.route('/teams/')
@app.route('/teams/<int:page>')
@login_required
def teams(page=1):
	"""Page - All New Mexico teams"""
	teams = Team.query.paginate(page, ITEMS_PER_PAGE, False)
	print 'teams', teams
	return render_template('teams.html', title="Mission Teams", \
							teams=teams)

@app.route('/team/<int:id>')
@login_required
def team(id):
	"""Page - Team Page"""
	team = Team.query.get(int(id))
	return render_template('team.html', title="Mission Teams", \
							team=team)

@app.route('/kids/')
@app.route('/kids/<int:page>')
@login_required
def kids(page=1):
	"""Page - All New Mexico Kids from LWRC"""
	kids = Kid.query.paginate(page, ITEMS_PER_PAGE, False)
	return render_template('kids.html', title="New Mexico Kids", \
							kids=kids)

@app.route('/kid/<int:id>')
@login_required
def kid(id):
	"""Page - All New Mexico Kids from LWRC"""
	kid = Kid.query.get(int(id))
	return render_template('kid.html', title="Kid Information", \
							kid=kid)

@app.route('/header/')
def header():
	return render_template('header.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
	loginform = LoginForm()
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('index'))

	if loginform.validate_on_submit():
		user = loginform.validate()
		if user:
			remember_me = loginform.remember_me.data
			login_user(user, remember_me)

			return loginform.redirect(next or url_for('index'))
	return render_template('login.html', title='Sign In', loginform=loginform)


@app.route('/logout/', methods=['GET'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.errorhandler(500)
def internal_error(exception):
	app.logger.error(exception)
	return render_template('500.html'), 500