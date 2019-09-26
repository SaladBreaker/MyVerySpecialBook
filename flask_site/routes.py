from flask_site.app import app
from flask import render_template, url_for, redirect, flash
import random
import json


@app.route("/")
@app.route("/home")
def home():
    return render_template("test.html")
