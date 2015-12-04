from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = "/login"
lm.login_message = """You must be a member of New Mexico Mission Team. 
					Please ask the administrator for New Mexico Missions Web Site
					for user credentials."""
lm.login_message_category = "info"

#logging
if not app.debug:
	import logging
	from logging import Formatter, getLogger
	from logging.handlers import RotatingFileHandler
	file_handler = RotatingFileHandler('flask.log', maxBytes=1024*1024*100, backupCount=20)
	file_handler.setLevel(logging.ERROR)
	file_handler.setFormatter(Formatter(
		'%(asctime)s - %(levelname)s: %(message)s '
		'[in %(pathname)s:%(lineno)d]'
	))
	loggers = [app.logger, getLogger('sqlalchemy')]
	for logger in loggers:
		logger.addHandler(file_handler)

from src import views
from src.models import user