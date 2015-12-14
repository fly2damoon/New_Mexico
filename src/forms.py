from flask import request, url_for, redirect
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, HiddenField
from wtforms.validators import DataRequired
from src.models.user import User, Team, Kid
from urlparse import urlparse, urljoin

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
            ref_url.netloc == test_url.netloc

def get_redirect_target():
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target


class RedirectForm(Form):
    next = HiddenField()

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        if not self.next.data:
            self.next.data = get_redirect_target() or ''

    def redirect(self, endpoint='index', **values):
        if is_safe_url(self.next.data):
            return redirect(self.next.data)
        target = get_redirect_target()
        return redirect(target or url_for(endpoint, **values))


class LoginForm(RedirectForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

    def validate(self):
        #run wtforms.validators
        if not Form.validate(self):
            return False

        user = User.query.filter_by(username=self.username.data.lower()).first()
        #username exists in db
        if user:
            #check password
            if user.verify_password(self.password.data):
                return user
            else:
                #APPEND ERROR MESSAGE - Password Mismatch
                self.password.errors.append('Password does not match')
                return False
        else:
            #APPEND ERROR MESSAGE - Invalid Username
            self.username.errors.append('Username not found')
            return False


class TeamAddForm(RedirectForm):
    year = StringField('year', validators=[DataRequired()])
    theme = StringField('theme', validators=[DataRequired()])
    verse = StringField('verse', validators=[DataRequired()])

    def validate(self):
        #run wtforms.validators
        if not Form.validate(self):
            return False

        team = Team.query.filter_by(year=self.year.data.lower()).first()
        #team already exists in db
        if team:
            self.year.errors.append('Team\'s year already exists')
            return False
        else:
            team = Team(year=self.year.data, theme=self.theme.data, verse=self.verse.data)
            team.add()
            return team
            #APPEND ERROR MESSAGE - Invalid Username

class KidAddForm(RedirectForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name')
    gender = StringField('gender')
    birthdate = StringField('birthdate')
    year = StringField('year')
    tribe = StringField('tribe')
    prayer = StringField('prayer')
    notes = StringField('notes')

    def validate(self):
        print ("inside validate")
        #run wtforms.validators
        if not Form.validate(self):
            return False

        kid = Kid(first_name=self.first_name.data, last_name=self.last_name.data, gender=self.gender.data, \
                   birthdate=self.birthdate.data, year=self.year.data, tribe=self.tribe.data, \
                   prayer=self.prayer.data, notes=self.notes.data)

        kid.add()
        return kid
        #APPEND ERROR MESSAGE - Invalid Username