from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/request')
def path():

    r1 = requests.get("http://service1:5001")
    r2 = requests.get("http://service2:5002")
    r3 = requests.get("http://service3:5003")

    return r2, r1, r3

