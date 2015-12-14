from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
skit = Table('skit', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x1052c3dd0; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f1d0; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f090; now>)),
    Column('title', Text),
    Column('story', Text),
    Column('team_id', Integer),
)

member = Table('member', pre_meta,
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

member = Table('member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x1052c3dd0; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f1d0; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f090; now>)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('gender', String(length=10)),
    Column('mobile_number', Integer),
    Column('email', String(length=120)),
    Column('birthdate', DateTime),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x1052c3dd0; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f1d0; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f090; now>)),
    Column('username', String(length=40)),
    Column('password_hash', String(length=128)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('email', String(length=120)),
)

team = Table('team', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('year', INTEGER),
    Column('theme', TEXT),
    Column('verse', TEXT),
    Column('email', VARCHAR(length=120)),
    Column('created_at', TIMESTAMP),
    Column('modified_at', TIMESTAMP),
)

team = Table('team', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x1052c3dd0; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f1d0; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f090; now>)),
    Column('year', Integer),
    Column('theme', Text),
    Column('verse', Text),
    Column('email', String(length=120)),
)

post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=200)),
    Column('body', TEXT),
    Column('created_by', INTEGER),
    Column('created_at', TIMESTAMP),
    Column('modified_at', TIMESTAMP),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x1052c3dd0; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f1d0; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f090; now>)),
    Column('title', String(length=200)),
    Column('body', Text),
    Column('created_by', Integer),
)

kid = Table('kid', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('first_name', VARCHAR(length=50)),
    Column('last_name', VARCHAR(length=50)),
    Column('gender', VARCHAR(length=10)),
    Column('birthdate', TIMESTAMP),
    Column('year', TIMESTAMP),
    Column('tribe', VARCHAR(length=50)),
    Column('prayer', TEXT),
    Column('notes', TEXT),
    Column('created_at', TIMESTAMP),
    Column('modified_at', TIMESTAMP),
)

kid = Table('kid', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x1052c3dd0; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f1d0; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x10530f090; now>)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('gender', String(length=10)),
    Column('birthdate', DateTime),
    Column('year', DateTime),
    Column('tribe', String(length=50)),
    Column('prayer', Text),
    Column('notes', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skit'].columns['created_on'].create()
    post_meta.tables['skit'].columns['updated_on'].create()
    pre_meta.tables['member'].columns['created_at'].drop()
    pre_meta.tables['member'].columns['modified_at'].drop()
    post_meta.tables['member'].columns['created_on'].create()
    post_meta.tables['member'].columns['updated_on'].create()
    post_meta.tables['user'].columns['created_on'].create()
    post_meta.tables['user'].columns['updated_on'].create()
    pre_meta.tables['team'].columns['created_at'].drop()
    pre_meta.tables['team'].columns['modified_at'].drop()
    post_meta.tables['team'].columns['created_on'].create()
    post_meta.tables['team'].columns['updated_on'].create()
    pre_meta.tables['post'].columns['created_at'].drop()
    pre_meta.tables['post'].columns['modified_at'].drop()
    post_meta.tables['post'].columns['created_on'].create()
    post_meta.tables['post'].columns['updated_on'].create()
    pre_meta.tables['kid'].columns['created_at'].drop()
    pre_meta.tables['kid'].columns['modified_at'].drop()
    post_meta.tables['kid'].columns['created_on'].create()
    post_meta.tables['kid'].columns['updated_on'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skit'].columns['created_on'].drop()
    post_meta.tables['skit'].columns['updated_on'].drop()
    pre_meta.tables['member'].columns['created_at'].create()
    pre_meta.tables['member'].columns['modified_at'].create()
    post_meta.tables['member'].columns['created_on'].drop()
    post_meta.tables['member'].columns['updated_on'].drop()
    post_meta.tables['user'].columns['created_on'].drop()
    post_meta.tables['user'].columns['updated_on'].drop()
    pre_meta.tables['team'].columns['created_at'].create()
    pre_meta.tables['team'].columns['modified_at'].create()
    post_meta.tables['team'].columns['created_on'].drop()
    post_meta.tables['team'].columns['updated_on'].drop()
    pre_meta.tables['post'].columns['created_at'].create()
    pre_meta.tables['post'].columns['modified_at'].create()
    post_meta.tables['post'].columns['created_on'].drop()
    post_meta.tables['post'].columns['updated_on'].drop()
    pre_meta.tables['kid'].columns['created_at'].create()
    pre_meta.tables['kid'].columns['modified_at'].create()
    post_meta.tables['kid'].columns['created_on'].drop()
    post_meta.tables['kid'].columns['updated_on'].drop()
