from flask import Flask
import logging
from config import DB_CONFIG
from flask_wtf.csrf import CSRFProtect

logger = logging.getLogger(__name__)


app = Flask(__name__)
app.config["SECRET_KEY"] = "qSrbDdD5vTM4XEiG"
csrf = CSRFProtect(app)
csrf.init_app(app)


# DB config
from flask_sqlalchemy import SQLAlchemy

DB_URL = f"postgresql+psycopg2://{DB_CONFIG['USER']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['URL']}/{DB_CONFIG['DB_NAME']}"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # silence the deprecation warning
db = SQLAlchemy(app)
logger.debug("Database loaded!")
import flask_site.routes
