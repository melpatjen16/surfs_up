from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/skill_drill')
def skill_drill():
    return 'This is a skill drill'