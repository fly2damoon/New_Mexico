from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
teammember = Table('teammember', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('team_id', INTEGER),
    Column('member_id', INTEGER),
)

team_member = Table('team_member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('team_id', Integer),
    Column('member_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=40)),
    Column('password_hash', VARCHAR(length=128)),
    Column('first_name', VARCHAR(length=50)),
    Column('last_name', VARCHAR(length=50)),
    Column('email', VARCHAR(length=120)),
    Column('created_at', TIMESTAMP),
    Column('modified_at', TIMESTAMP),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['teammember'].drop()
    post_meta.tables['team_member'].create()
    pre_meta.tables['user'].columns['created_at'].drop()
    pre_meta.tables['user'].columns['modified_at'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['teammember'].create()
    post_meta.tables['team_member'].drop()
    pre_meta.tables['user'].columns['created_at'].create()
    pre_meta.tables['user'].columns['modified_at'].create()
