from application import app
from flask import render_template, request, redirect, url_for, Response, jsonify
from application.forms import NameForm
import requests
import json

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/generator', methods=['GET', 'POST'])
def generator():
    form = NameForm()
    if form.validate_on_submit:
        r4 = requests.post("http://service4:5004/home", json={"data":form.submit.data})
        r5 =  requests.get("http://service4:5004/home").json()["Result"]
        return r5
    return render_template('generator.html', title='Generator', form=form)
