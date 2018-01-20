from flask import Flask, render_template
from services.service import a

app = Flask(__name__)

@app.route('/')
def hello_world():
    a()
    return render_template('index.html.j2')