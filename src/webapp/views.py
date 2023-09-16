from datetime import datetime
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from .database import create_new_note, get_all_notes, delete_note_by_id
from typing import List
import uuid

views = Blueprint("views", __name__)


@views.route("/")
def index():
    return render_template("index.html", user=current_user)


@views.route("/home", methods=["GET", "POST", "PUT", "DELETE"])
@login_required
def home():
    notes: List[Note] = get_all_notes(current_user.id)

    if request.method == "POST":
        data = request.form
        note_title = data.get("title")
        note_content = data.get("content")

        if len(note_title) < 1:
            flash("Title is too short", "error")

        elif len(note_content) < 1:
            flash("Content is too short", "warning")
        else:
            new_note: Note = Note(
                id=uuid.uuid4(),
                user_id=current_user.id,
                title=note_title,
                content=note_content,
                created_at=datetime.utcnow(),
            )

            create_new_note(new_note)

            flash("Note successfully created and added", "success")

            return render_template("home.html", user=current_user, notes=get_all_notes(current_user.id))
        
    elif request.method == "DELETE":
        delete_note_by_id()
        
        return render_template("home.html", user=current_user, notes=get_all_notes(current_user.id))

    else:
        return render_template("home.html", user=current_user, notes=notes)
