from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, \
                            check_password_hash
from flask.ext.login import current_user
from sqlalchemy.ext.declarative import declared_attr
from src import app
from datetime import datetime

# class Base(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     created_at = db.Column(db.DateTime)
#     modified_at = db.Column(db.DateTime)


# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base(cls=CommonBase)

def _current_user_id_or_none():
    try:
        return current_user.id
    except:
        return None


class Base(db.Model):
    __abstract__ = True
    #id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @declared_attr
    def created_by_id(cls):
        return db.Column(db.Integer,
            db.ForeignKey('user.id', name='fk_%s_created_by_id' % cls.__name__, use_alter=True),
            # nullable=False,
            default=_current_user_id_or_none
        )

    @declared_attr
    def created_by(cls):
        return db.relationship(
            'User',
            primaryjoin='user.id == %s.created_by_id' % cls.__name__,
            remote_side='user.id'
        )

    @declared_attr
    def updated_by_id(cls):
        return db.Column(db.Integer,
            db.ForeignKey('user.id', name='fk_%s_updated_by_id' % cls.__name__, use_alter=True),
            # nullable=False,
            default=_current_user_id_or_none,
            onupdate=_current_user_id_or_none
        )

    @declared_attr
    def updated_by(cls):
        return db.relationship(
            'User',
            primaryjoin='user.id == %s.updated_by_id' % cls.__name__,
            remote_side='user.id'
        )

    # @classmethod
    # def add(self):
    #     db.session.add(self)
    #     db.session.commit()
    #     return self
    #
    # @classmethod
    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
    #     return self


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

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
        except Exception as e:
            app.logger.error(e)

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    def __init__(self, username, password, first_name, last_name, email):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return 'User: {0} {1}'.format(self.first_name, self.last_name)


teammember = db.Table('team_member', 
    db.Column('id', db.Integer, primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
    db.Column('member_id', db.Integer, db.ForeignKey('member.id'))
)

class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    mobile_number = db.Column(db.Integer)
    email = db.Column(db.String(120))
    birthdate = db.Column(db.DateTime)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
            return 'Member: {0} {1}'.format(self.first_name, self.last_name)


class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    theme = db.Column(db.Text)
    verse = db.Column(db.Text)
    email = db.Column(db.String(120), unique=True)
    members = db.relationship('Member', secondary=teammember,
        backref=db.backref('Team', lazy='dynamic'))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
            return 'Team:  {0}'.format(self.year)


class Kid(db.Model):
    __tablename__ = 'kid'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    birthdate = db.Column(db.DateTime)
    year = db.Column(db.DateTime)
    tribe = db.Column(db.String(50))
    prayer = db.Column(db.Text)
    notes = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
            return 'Kid: {0} {1}'.format(self.first_name, self.last_name)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
            return 'Post: {0} - {1}'.format(self.title, self.body)


kidPost = db.Table('kid_post', 
    db.Column('id', db.Integer, primary_key=True),
    db.Column('kid_id', db.Integer, db.ForeignKey('kid.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)


class Skit(db.Model):
    __tablename__ = 'skit'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    story = db.Column(db.Text)
    team_id = db.Column(db.Integer, 
                        db.ForeignKey('team.id', ondelete='CASCADE'))
    team = db.relationship('Team')
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


skitmember = db.Table('skit_member',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('skit_id', db.Integer, db.ForeignKey('skit.id')),
    db.Column('member_id', db.Integer, db.ForeignKey('member.id')))


#games, classes, leaders(?), 