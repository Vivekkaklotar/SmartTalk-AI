from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime

# Config
class Config:
    SECRET_KEY = 'smarttalk-ai-2024'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///smarttalk.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Initialize
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="trainee")

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.Text)
    response = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Knowledge Base (NO EMOJI)
KNOWLEDGE_BASE = {
    "python string": {
        "title": "Python Strings",
        "desc": "String methods:\n• upper(), lower()\n• split(), join()\n• strip(), replace()\n• f-strings",
        "code": 'text = "Hello"\nprint(text.upper())\nprint(f"Hi {text}")'
    },
    "python list": {
        "title": "Python Lists", 
        "desc": "List operations:\n• append(), remove()\n• list comprehension\n• slicing",
        "code": 'arr = [1,2,3]\narr.append(4)\nprint([x*2 for x in arr])'
    },
    "flask route": {
        "title": "Flask Route",
        "desc": "@app.route():\n• GET/POST methods\n• dynamic routes\n• render_template()",
        "code": '@app.route("/")\ndef home():\n    return "Hello World!"'
    },
    "binary search": {
        "title": "Binary Search",
        "desc": "O(log n) algorithm:\n• sorted array\n• divide & conquer\n• mid check",
        "code": 'def binary_search(arr, x):\n    l, r = 0, len(arr)-1\n    while l <= r:\n        m = (l+r)//2\n        if arr[m] == x: return m\n        elif arr[m] < x: l = m+1\n    return -1'
    }
}

# 🔥 UPDATED SMART MATCHING
def get_response(message):
    msg = message.lower().strip()

    for key in KNOWLEDGE_BASE:
        words = key.split()
        if all(word in msg for word in words):
            return KNOWLEDGE_BASE[key]

    return {
        "title": "SmartTalk Assistant",
        "desc": "Try:\npython string\npython list\nflask route\nbinary search",
        "code": ""
    }

# Routes
@app.route("/")
def home():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash("Wrong credentials!")
    
    return render_template("login.html")

@app.route("/register", methods=['POST'])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if User.query.filter_by(username=username).first():
        flash("User exists!")
        return redirect(url_for('login'))
    
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    role = "owner" if username.lower() == "vivek" else "trainee"
    user = User(username=username, password=hashed, role=role)
    db.session.add(user)
    db.session.commit()
    flash("Registered!")
    return redirect(url_for('login'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@app.route("/chat")
@login_required
def chat():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
@login_required
def ask():
    data = request.get_json()
    user_msg = data.get("message", "")

    bot = get_response(user_msg)

    chat = Chat(user_id=current_user.id, message=user_msg, response=bot["desc"])
    db.session.add(chat)
    db.session.commit()

    return jsonify(bot)

@app.route("/owner")
@login_required
def owner():
    if current_user.role != "owner":
        flash("Owner only!")
        return redirect(url_for('dashboard'))
    return render_template("owner.html")

# Create DB
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)