import random
import re

# 🚀 Enhanced Knowledge Base - Professional Topics
KNOWLEDGE_BASE = {
    # PYTHON TOPICS
    "python": {
        "string": {
            "title": "🐍 Python Strings - Complete Guide",
            "desc": "Strings immutable text data store karte hain:\n\n🔹 **Methods:**\n• `.upper()`, `.lower()`, `.title()`\n• `.strip()`, `.lstrip()`, `.rstrip()`\n• `.split()`, `.join()`, `.replace()`\n• `.find()`, `.index()`, `.startswith()`\n\n🔹 **Formatting:**\n• f-strings: `f'Hello {name}'`\n• `.format()` method",
            "code": '''# String Operations
text = "  Hello World  "
print(text.strip())      # "Hello World"
print(text.upper())      # "  HELLO WORLD  "
print(text.split())      # ['Hello', 'World']

# F-strings (Python 3.6+)
name = "Vivek"
age = 22
print(f"Hello {name}, age {age}")  # Hello Vivek, age 22

# Formatting
print("Price: ${:.2f}".format(19.999))  # Price: $20.00'''
        },
        "list": {
            "title": "📋 Python Lists - Advanced",
            "desc": "Mutable ordered collections:\n\n🔹 **Methods:**\n• `append()`, `extend()`, `insert()`\n• `pop()`, `remove()`, `clear()`\n• `index()`, `count()`, `sort()`\n\n🔹 **Comprehensions:**\n• `[x for x in lst if condition]`",
            "code": '''# List Operations
fruits = ["apple", "banana", "cherry"]

# Add/Remove
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
print(fruits)  # ['apple', 'mango', 'cherry', 'orange']

# List Comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]

# Slicing
print(fruits[1:3])  # ['mango', 'cherry']'''
        },
        "dict": {
            "title": "🎯 Python Dictionaries - Pro Tips",
            "desc": "Key-value pairs (Hash Maps):\n\n🔹 **Methods:**\n• `get()`, `setdefault()`\n• `keys()`, `values()`, `items()`\n• `pop()`, `popitem()`, `update()`\n\n🔹 **Dict Comprehension:**\n• `{k: v for k, v in items}`",
            "code": '''# Dictionary Operations
user = {
    "name": "Vivek",
    "age": 22,
    "skills": ["Python", "Flask", "HTML"]
}

# Safe access
name = user.get("name", "Unknown")
print(name)  # Vivek

# Dict Comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Update
user.update({"role": "Developer"})
print(user["role"])  # Developer'''
        },
        "function": {
            "title": "⚙️ Python Functions - Masterclass",
            "desc": "Reusable code blocks:\n\n🔹 **Types:**\n• Default args, `*args`, `**kwargs`\n• Lambda functions\n• Decorators\n• Generators (`yield`)\n\n🔹 **Best Practices:**\n• Docstrings\n• Type hints",
            "code": '''def calculate_total(price, tax=0.1, discount=0.0):
    """Calculate final price with tax & discount"""
    total = price * (1 + tax) * (1 - discount)
    return round(total, 2)

# *args, **kwargs
def process_data(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

process_data(1, 2, 3, name="Vivek", age=22)

# Lambda
double = lambda x: x * 2
print(double(5))  # 10

# Generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b'''
        },
        "oop": {
            "title": "🏗️ Python OOP - Classes & Objects",
            "desc": "Object-Oriented Programming:\n\n🔹 **Concepts:**\n• Classes, Objects\n• `__init__`, `__str__`\n• Inheritance, Polymorphism\n• `@property`, `@staticmethod`",
            "code": '''class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
    
    def __str__(self):
        return f"Student: {self.name}, Age: {self._age}"

# Inheritance
class Developer(Student):
    def __init__(self, name, age, skills):
        super().__init__(name, age)
        self.skills = skills

dev = Developer("Vivek", 22, ["Python", "Flask"])
print(dev)  # Student: Vivek, Age: 22'''
        }
    },
    
    # FLASK WEB DEVELOPMENT
    "flask": {
        "route": {
            "title": "🌐 Flask Routes - Web Development",
            "desc": "Create web endpoints:\n\n🔹 **Decorators:**\n• `@app.route()`\n• `methods=['GET', 'POST']`\n• `strict_slashes=False`\n\n🔹 **Templates:**\n• `render_template()`\n• Jinja2 syntax",
            "code": '''from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="SmartTalk")

@app.route("/api/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        data = request.json
        return jsonify({"status": "created", "data": data})
    return jsonify({"users": ["Vivek", "Admin"]})

@app.route("/user/<name>")
def profile(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)'''
        },
        "form": {
            "title": "📝 Flask Forms & Validation",
            "desc": "Handle user input safely:\n\n🔹 **WTForms:**\n• Form validation\n• CSRF protection\n• File uploads\n\n🔹 **Manual:**\n• `request.form`\n• `request.files`",
            "code": '''from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        # Process login
        return f"Welcome {username}!"
    return render_template("login.html", form=form)'''
        }
    },
    
    # DATA STRUCTURES & ALGORITHMS
    "algorithm": {
        "binary": {
            "title": "🔍 Binary Search - O(log n)",
            "desc": "Fast search in sorted arrays:\n\n🔹 **Time:** O(log n)\n🔹 **Space:** O(1)\n🔹 **Steps:**\n1. Find middle\n2. Compare target\n3. Eliminate half\n4. Repeat",
            "code": '''def binary_search(arr, target):
    """Binary search on sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Usage
numbers = [1, 3, 5, 7, 9, 11, 13]
index = binary_search(numbers, 7)
print(f"Found at index: {index}")  # 3'''
        },
        "bubble": {
            "title": "🫧 Bubble Sort - O(n²)",
            "desc": "Simple comparison sort:\n\n🔹 **Time:** O(n²)\n🔹 **Space:** O(1)\n🔹 **Stable:** Yes\n🔹 **Best for:** Small datasets",
            "code": '''def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))  # [11, 12, 22, 25, 34, 64, 90]'''
        }
    },
    
    # JAVASCRIPT
    "javascript": {
        "arrow": {
            "title": "⚡ JavaScript Arrow Functions",
            "desc": "ES6+ concise functions:\n\n🔹 **Syntax:** `() => {}`\n🔹 **No `this` binding\n🔹 **Implicit return\n🔹 **Perfect for:** Callbacks, React",
            "code": '''// Arrow Functions
const add = (a, b) => a + b;
const multiply = (a, b) => {
    return a * b;
};

const users = ['Vivek', 'Admin'];
const greet = users.map(user => `Hello ${user}!`);

// Async/Await
const fetchData = async () => {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
};'''
        }
    },
    
    # GENERAL PROGRAMMING
    "debug": {
        "title": "🐛 Debugging Pro Tips",
        "desc": "Common debugging techniques:\n\n🔹 **Python:**\n• `print()` statements\n• `pdb` debugger\n• `logging` module\n\n🔹 **Browser:**\n• Console.log()\n• Network tab\n• Breakpoints",
        "code": '''import logging
import pdb

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def buggy_function(x):
    logger.debug(f"Input: {x}")
    if x < 0:
        logger.warning("Negative input!")
        pdb.set_trace()  # Debugger
    return x * 2

# Usage
result = buggy_function(-5)
print(result)'''
    }
}

# FALLBACK RESPONSES
FALLBACKS = [
    "🤔 Yeh topic abhi available nahi hai. Try karo:\n• 'python string'\n• 'flask route'\n• 'binary search'\n• 'java loop'",
    "🔍 Search kar raha hu... Abhi ye nahi mila. Popular topics:\n• Python lists/functions\n• Flask routes/forms\n• Algorithms (binary search)",
    "💡 Suggestion: 'python dict', 'flask form', ya 'javascript arrow' try karo!"
]

def get_response(message):
    """Smart response generator"""
    msg = message.lower().strip()
    
    # Exact keyword matching
    for category, topics in KNOWLEDGE_BASE.items():
        if category in msg:
            for topic, data in topics.items():
                if topic in msg:
                    return data
    
    # Partial matching
    for category, topics in KNOWLEDGE_BASE.items():
        for topic, data in topics.items():
            if topic in msg or category in msg:
                return data
    
    # Fallback
    return {
        "title": "🔎 Topic Not Found",
        "desc": random.choice(FALLBACKS),
        "code": ""
    }

# Usage Example
if __name__ == "__main__":
    print(get_response("python string"))
    print(get_response("flask"))