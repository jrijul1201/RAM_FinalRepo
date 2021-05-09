from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Please elaborate more', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Service Added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/about', methods=['GET', 'POST'])
def about():
        return render_template("about.html", user=current_user)
@views.route('/', methods=['GET', 'POST'])
def index():
        return render_template("index.html", user=current_user)
    
@views.route('/company', methods=['GET', 'POST'])
def company():
        return render_template("company.html", user=current_user)
@views.route('/furnitures', methods=['GET', 'POST'])
def furnitures():
        return render_template("furnitures.html", user=current_user)
    

@views.route('/contact', methods=['GET', 'POST'])
def contact():
        return render_template("contact.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
