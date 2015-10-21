from flask import render_template, session, redirect, url_for, current_app
from ..models import Manufacturer
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    manufacturers = Manufacturer.query.order_by(Manufacturer.name).all()
    return render_template('index.html', manufacturers=manufacturers)
