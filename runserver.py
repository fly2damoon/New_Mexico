from src import app
import logging
import logging.config

logging.config.fileConfig("log.conf")
logging.info("info log")
logging.info("info log 2")

logging.exception("exception log")
logging.exception("exception log 2")

app.run(debug=True)