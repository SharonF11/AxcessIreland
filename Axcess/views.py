from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html", user=current_user)


@views.route('/subscription', methods=['GET', 'POST'])
def subscription():
    if request.method == 'GET':
        return render_template("subscription.html", user=current_user)

    return jsonify({})
