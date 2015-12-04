from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
posts = Table('posts', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=200)),
    Column('body', Text),
    Column('created_by', Integer),
    Column('created_at', DateTime),
    Column('modified_at', DateTime),
)

kids = Table('kids', post_meta,
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

users = Table('users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=40)),
    Column('password_hash', String(length=128)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('email', String(length=120)),
    Column('created_at', DateTime),
    Column('modified_at', DateTime),
)

members = Table('members', post_meta,
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

teams = Table('teams', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('year', Integer),
    Column('theme', Text),
    Column('verse', Text),
    Column('email', String(length=120)),
    Column('created_at', DateTime),
    Column('modified_at', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['posts'].create()
    post_meta.tables['kids'].columns['created_at'].create()
    post_meta.tables['kids'].columns['modified_at'].create()
    post_meta.tables['users'].columns['created_at'].create()
    post_meta.tables['users'].columns['modified_at'].create()
    post_meta.tables['members'].columns['created_at'].create()
    post_meta.tables['members'].columns['modified_at'].create()
    post_meta.tables['teams'].columns['created_at'].create()
    post_meta.tables['teams'].columns['modified_at'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['posts'].drop()
    post_meta.tables['kids'].columns['created_at'].drop()
    post_meta.tables['kids'].columns['modified_at'].drop()
    post_meta.tables['users'].columns['created_at'].drop()
    post_meta.tables['users'].columns['modified_at'].drop()
    post_meta.tables['members'].columns['created_at'].drop()
    post_meta.tables['members'].columns['modified_at'].drop()
    post_meta.tables['teams'].columns['created_at'].drop()
    post_meta.tables['teams'].columns['modified_at'].drop()
