from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    # To make sure any failed database sessions do not
    # interfere with any database accesses triggered by
    # the template we use rollback()
    db.session.rollback()
    return render_template("500.html"), 500
