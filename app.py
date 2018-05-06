from flask import Flask
from flask import request
from voiceroid import Voiceroid2

app = Flask(__name__)
voiceroid = Voiceroid2()

@app.route('/talk')
def talk():
    speaker = request.args.get("speaker")
    sentence = request.args.get("sentence")
    voiceroid.talk(speaker, sentence)
    return "ok"

@app.route("/")
def hello():
    return "Hello World"