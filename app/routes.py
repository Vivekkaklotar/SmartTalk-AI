from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .chatbot import get_response
from .models import Chat
from . import db

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return redirect(url_for('auth.login'))


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@main.route("/chat")
@login_required
def chat():
    return render_template("chat.html")


@main.route("/ask", methods=["POST"])
@login_required
def ask():

    data = request.get_json()
    user_msg = data.get("message")

    bot = get_response(user_msg)

    chat = Chat(
        user_id=current_user.id,
        message=user_msg,
        response=bot["desc"]
    )

    db.session.add(chat)
    db.session.commit()

    return jsonify(bot)


@main.route("/owner")
@login_required
def owner_panel():
    return render_template("owner.html")