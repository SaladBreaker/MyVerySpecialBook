from flask import Flask
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

import flask_site.routes
