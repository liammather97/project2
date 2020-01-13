from flask import render_template, redirect, url_for, jsonify
from application import app
import json

@app.route('/')
@app.route('/home',methods=('GET','POST'))
def home(json):
    request.get(service2).json()
    request.get(service3).json()
    user_input=request.get_json('data')
    combined = prefix1 + user_input + suffix1
    result = jsonify({"Result":combined})
    return result


