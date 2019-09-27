from flask_site.app import app
from flask import render_template, url_for, redirect, flash
import random
import json


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/allbooks")
def allbooks():
    return render_template("allbooks.html")


@app.route("/addbook")
def addbook():
    return render_template("addbook.html")


@app.route("/addfile")
def addfile():
    return render_template("addfile.html")
