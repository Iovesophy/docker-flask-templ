from flask import Flask
import datetime

app = Flask(__name__)

def today_builder():
    hello = "<p>Hello, World!</p>"
    br = "<br />"
    text = "<p>This page can show date info.</p>"
    dt = datetime.date.today()
    return hello + text + br + "today: " + str(dt)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/today")
def today():
  return today_builder()
