from application import app
from flask import render_template, request, redirect, url_for, Response
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
        r2 = requests.get("http://service2:5002/")
        r3 = requests.get("http://service3:5003/")
        data = {"prefix":r2["choice"],"suffix":r3["choice"],"user_input":form.name.data}
        r4 = requests.post("http://service4:5004/", json=data)
        return r4["Result"]
    return render_template('generator.html', title='Generator', form=form)

