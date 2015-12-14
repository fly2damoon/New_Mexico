from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
skit = Table('skit', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79050; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79410; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c792d0; now>)),
    Column('title', Text),
    Column('story', Text),
    Column('team_id', Integer),
    Column('updated_by_id', Integer, onupdate=ColumnDefault(<function <lambda> at 0x106c44de8>), default=ColumnDefault(<function <lambda> at 0x106c44140>)),
    Column('created_by_id', Integer, default=ColumnDefault(<function <lambda> at 0x106c44ed8>)),
)

member = Table('member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79050; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79410; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c792d0; now>)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('gender', String(length=10)),
    Column('mobile_number', Integer),
    Column('email', String(length=120)),
    Column('birthdate', DateTime),
    Column('updated_by_id', Integer, onupdate=ColumnDefault(<function <lambda> at 0x106c7bf50>), default=ColumnDefault(<function <lambda> at 0x106c7bed8>)),
    Column('created_by_id', Integer, default=ColumnDefault(<function <lambda> at 0x106ca70c8>)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79050; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79410; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c792d0; now>)),
    Column('username', String(length=40)),
    Column('password_hash', String(length=128)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('email', String(length=120)),
    Column('updated_by_id', Integer, onupdate=ColumnDefault(<function <lambda> at 0x106c7b230>), default=ColumnDefault(<function <lambda> at 0x106c7b1b8>)),
    Column('created_by_id', Integer, default=ColumnDefault(<function <lambda> at 0x106c7b320>)),
)

team = Table('team', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79050; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79410; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c792d0; now>)),
    Column('year', Integer),
    Column('theme', Text),
    Column('verse', Text),
    Column('email', String(length=120)),
    Column('updated_by_id', Integer, onupdate=ColumnDefault(<function <lambda> at 0x106ca77d0>), default=ColumnDefault(<function <lambda> at 0x106ca7758>)),
    Column('created_by_id', Integer, default=ColumnDefault(<function <lambda> at 0x106ca78c0>)),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79050; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79410; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c792d0; now>)),
    Column('title', String(length=200)),
    Column('body', Text),
    Column('created_by', Integer),
    Column('updated_by_id', Integer, onupdate=ColumnDefault(<function <lambda> at 0x106c44758>), default=ColumnDefault(<function <lambda> at 0x106c446e0>)),
    Column('created_by_id', Integer, default=ColumnDefault(<function <lambda> at 0x106c44848>)),
)

kid = Table('kid', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79050; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c79410; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x106c792d0; now>)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('gender', String(length=10)),
    Column('birthdate', DateTime),
    Column('year', DateTime),
    Column('tribe', String(length=50)),
    Column('prayer', Text),
    Column('notes', Text),
    Column('updated_by_id', Integer, onupdate=ColumnDefault(<function <lambda> at 0x106ca7de8>), default=ColumnDefault(<function <lambda> at 0x106ca7e60>)),
    Column('created_by_id', Integer, default=ColumnDefault(<function <lambda> at 0x106ca7cf8>)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skit'].columns['created_by_id'].create()
    post_meta.tables['skit'].columns['updated_by_id'].create()
    post_meta.tables['member'].columns['created_by_id'].create()
    post_meta.tables['member'].columns['updated_by_id'].create()
    post_meta.tables['user'].columns['created_by_id'].create()
    post_meta.tables['user'].columns['updated_by_id'].create()
    post_meta.tables['team'].columns['created_by_id'].create()
    post_meta.tables['team'].columns['updated_by_id'].create()
    post_meta.tables['post'].columns['created_by_id'].create()
    post_meta.tables['post'].columns['updated_by_id'].create()
    post_meta.tables['kid'].columns['created_by_id'].create()
    post_meta.tables['kid'].columns['updated_by_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skit'].columns['created_by_id'].drop()
    post_meta.tables['skit'].columns['updated_by_id'].drop()
    post_meta.tables['member'].columns['created_by_id'].drop()
    post_meta.tables['member'].columns['updated_by_id'].drop()
    post_meta.tables['user'].columns['created_by_id'].drop()
    post_meta.tables['user'].columns['updated_by_id'].drop()
    post_meta.tables['team'].columns['created_by_id'].drop()
    post_meta.tables['team'].columns['updated_by_id'].drop()
    post_meta.tables['post'].columns['created_by_id'].drop()
    post_meta.tables['post'].columns['updated_by_id'].drop()
    post_meta.tables['kid'].columns['created_by_id'].drop()
    post_meta.tables['kid'].columns['updated_by_id'].drop()
