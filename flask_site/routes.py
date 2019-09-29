from flask_site.app import app, db
from flask import render_template, url_for, redirect, flash, request
from flask_site.forms import AddBookForm
from flask_site.models import Book
import random
import json

import logging

logger = logging.getLogger(__name__)


def get_all_books():
    return Book.query.order_by(Book.title).all()


@app.route("/")
@app.route("/home")
def home():
    get_all_books()
    return render_template("home.html")


@app.route("/allbooks")
def allbooks():
    return render_template("allbooks.html", books=get_all_books())


@app.route("/addbook", methods=["GET", "POST"])
def addbook():
    form = AddBookForm()

    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data)

        try:
            db.session.add(book)
            db.session.commit()

        except Exception as e:
            logger.warning(f"Could not save book in database. Error: {e}")
            flash("Unexpected error at adding book. Please try again!", "danger")
            return redirect(url_for("home"))

        flash("Book added!", "addbook")
        return redirect(url_for("allbooks", books=get_all_books()))

    return render_template("addbook.html", form=form)


@app.route("/addfile")
def addfile():
    return render_template("addfile.html")
