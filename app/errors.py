from flask import render_template
from .flask_app import app
from .db import DB


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    DB.session.rollback() # TODO: fix this
    return render_template('errors/500.html'), 500


@app.errorhandler(502)
def bad_gateway_error(error):
    return render_template('errors/502.html'), 502
