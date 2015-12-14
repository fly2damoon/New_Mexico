from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
skit = Table('skit', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', Text),
    Column('story', Text),
    Column('team_id', Integer),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e24110; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e243d0; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e242d0; now>)),
)

member = Table('member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('gender', String(length=10)),
    Column('mobile_number', Integer),
    Column('email', String(length=120)),
    Column('birthdate', DateTime),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e635d0; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e63890; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e63790; now>)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=40)),
    Column('password_hash', String(length=128)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('email', String(length=120)),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e0b810; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e0bad0; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e0b9d0; now>)),
)

team = Table('team', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('year', Integer),
    Column('theme', Text),
    Column('verse', Text),
    Column('email', String(length=120)),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e63f50; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e83250; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e83150; now>)),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=200)),
    Column('body', Text),
    Column('user_id', Integer),
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e8f450; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e8f710; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e8f610; now>)),
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
    Column('created_on', DateTime, default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e83a90; now>)),
    Column('updated_on', DateTime, onupdate=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e83dd0; now>), default=ColumnDefault(<sqlalchemy.sql.functions.now at 0x105e83cd0; now>)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skit'].columns['created_on'].create()
    post_meta.tables['skit'].columns['updated_on'].create()
    post_meta.tables['member'].columns['created_on'].create()
    post_meta.tables['member'].columns['updated_on'].create()
    post_meta.tables['user'].columns['created_on'].create()
    post_meta.tables['user'].columns['updated_on'].create()
    post_meta.tables['team'].columns['created_on'].create()
    post_meta.tables['team'].columns['updated_on'].create()
    post_meta.tables['post'].columns['created_on'].create()
    post_meta.tables['post'].columns['updated_on'].create()
    post_meta.tables['kid'].columns['created_on'].create()
    post_meta.tables['kid'].columns['updated_on'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['skit'].columns['created_on'].drop()
    post_meta.tables['skit'].columns['updated_on'].drop()
    post_meta.tables['member'].columns['created_on'].drop()
    post_meta.tables['member'].columns['updated_on'].drop()
    post_meta.tables['user'].columns['created_on'].drop()
    post_meta.tables['user'].columns['updated_on'].drop()
    post_meta.tables['team'].columns['created_on'].drop()
    post_meta.tables['team'].columns['updated_on'].drop()
    post_meta.tables['post'].columns['created_on'].drop()
    post_meta.tables['post'].columns['updated_on'].drop()
    post_meta.tables['kid'].columns['created_on'].drop()
    post_meta.tables['kid'].columns['updated_on'].drop()
