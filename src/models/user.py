from src import db
from werkzeug.security import generate_password_hash, \
                            check_password_hash

# class Base(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     created_at = db.Column(db.DateTime)
#     modified_at = db.Column(db.DateTime)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymouse(self):
        return False

    #@is_authenticated.setter
    #def authenticated(self, val):
        #self._is_authenticated = val
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        try:
            return unicode(self.id)
        except Exception, e:
            app.logger.error(e)

    def __init__(self, username, password, first_name, last_name, email):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return 'User: {0} {1}'.format(self.first_name, self.last_name)


teamMembers = db.Table('teamMembers', 
    db.Column('id', db.Integer, primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('teams.id')),
    db.Column('member_id', db.Integer, db.ForeignKey('members.id'))
)


class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    mobile_number = db.Column(db.Integer)
    email = db.Column(db.String(120))
    birthdate = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    
    def __repr__(self):
        return 'Member: {0} {1}'.format(self.first_name, self.last_name)


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    theme = db.Column(db.Text)
    verse = db.Column(db.Text)
    email = db.Column(db.String(120), unique=True)
    members = db.relationship('Member', secondary=teamMembers,
    	backref=db.backref('Team', lazy='dynamic'))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __repr__(self):
        return 'Team:  {0}'.format(self.year)


kidPosts = db.Table('kidposts', 
    db.Column('id', db.Integer, primary_key=True),
    db.Column('kid_id', db.Integer, db.ForeignKey('kids.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'))
)


class Kid(db.Model):
    __tablename__ = 'kids'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    birthdate = db.Column(db.DateTime)
    year = db.Column(db.DateTime)
    tribe = db.Column(db.String(50))
    prayer = db.Column(db.Text)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    
    def __repr__(self):
        return 'Kid: {0} {1}'.format(self.first_name, self.last_name)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __repr__(self):
        return 'Post: {0} - {1}'.format(self.title, self.body)

