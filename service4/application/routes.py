from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/request')
def path():

    r1 = requests.get("http://service1:5000")
    r2 = requests.get("http://service2:5000")
    r3 = requests.get("http://service3:5000")

    return r1.text, r2.text, r3.text