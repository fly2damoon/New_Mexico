from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
members = Table('members', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('first_name', VARCHAR(length=50)),
    Column('last_name', VARCHAR(length=50)),
    Column('gender', VARCHAR(length=10)),
    Column('mobile_number', INTEGER),
    Column('email', VARCHAR(length=120)),
    Column('birthdate', TIMESTAMP),
    Column('created_at', TIMESTAMP),
    Column('modified_at', TIMESTAMP),
)

posts = Table('posts', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=200)),
    Column('body', TEXT),
    Column('created_by', INTEGER),
    Column('created_at', TIMESTAMP),
    Column('modified_at', TIMESTAMP),
)

teamMembers = Table('teamMembers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('team_id', INTEGER),
    Column('member_id', INTEGER),
)

teams = Table('teams', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('year', INTEGER),
    Column('theme', TEXT),
    Column('verse', TEXT),
    Column('email', VARCHAR(length=120)),
    Column('created_at', TIMESTAMP),
    Column('modified_at', TIMESTAMP),
)

users = Table('users', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=40)),
    Column('password_hash', VARCHAR(length=128)),
    Column('first_name', VARCHAR(length=50)),
    Column('last_name', VARCHAR(length=50)),
    Column('email', VARCHAR(length=120)),
    Column('created_at', TIMESTAMP),
    Column('modified_at', TIMESTAMP),
)

kid = Table('kid', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('gender', String(length=10)),
    Column('birthdate', DateTime),
    Column('year', DateTime),
    Column('tribe', String(length=50)),
    Column('prayer', Text),
    Column('notes', Text),
    Column('created_at', DateTime),
    Column('modified_at', DateTime),
)

kid_post = Table('kid_post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('kid_id', Integer),
    Column('post_id', Integer),
)

member = Table('member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('gender', String(length=10)),
    Column('mobile_number', Integer),
    Column('email', String(length=120)),
    Column('birthdate', DateTime),
    Column('created_at', DateTime),
    Column('modified_at', DateTime),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=200)),
    Column('body', Text),
    Column('created_by', Integer),
    Column('created_at', DateTime),
    Column('modified_at', DateTime),
)

skit = Table('skit', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', Text),
    Column('story', Text),
    Column('team_id', Integer),
)

skit_member = Table('skit_member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('skit_id', Integer),
    Column('member_id', Integer),
)

team = Table('team', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('year', Integer),
    Column('theme', Text),
    Column('verse', Text),
    Column('email', String(length=120)),
    Column('created_at', DateTime),
    Column('modified_at', DateTime),
)

teamMember = Table('teamMember', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('team_id', Integer),
    Column('member_id', Integer),
)

teammember = Table('teammember', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('team_id', Integer),
    Column('member_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=40)),
    Column('password_hash', String(length=128)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('email', String(length=120)),
    Column('created_at', DateTime),
    Column('modified_at', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['members'].drop()
    pre_meta.tables['posts'].drop()
    pre_meta.tables['teamMembers'].drop()
    pre_meta.tables['teams'].drop()
    pre_meta.tables['users'].drop()
    post_meta.tables['kid'].create()
    post_meta.tables['kid_post'].create()
    post_meta.tables['member'].create()
    post_meta.tables['post'].create()
    post_meta.tables['skit'].create()
    post_meta.tables['skit_member'].create()
    post_meta.tables['team'].create()
    post_meta.tables['teamMember'].create()
    post_meta.tables['teammember'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['members'].create()
    pre_meta.tables['posts'].create()
    pre_meta.tables['teamMembers'].create()
    pre_meta.tables['teams'].create()
    pre_meta.tables['users'].create()
    post_meta.tables['kid'].drop()
    post_meta.tables['kid_post'].drop()
    post_meta.tables['member'].drop()
    post_meta.tables['post'].drop()
    post_meta.tables['skit'].drop()
    post_meta.tables['skit_member'].drop()
    post_meta.tables['team'].drop()
    post_meta.tables['teamMember'].drop()
    post_meta.tables['teammember'].drop()
    post_meta.tables['user'].drop()
