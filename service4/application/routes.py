from flask import render_template, redirect, url_for
from application import app

@app.route('/')
@app.route('/home',methods=('GET','POST'))
def home(json):
    prefix=json("prefix")
    suffix=json("suffix")
    user_input=json('user_input')
    combined = prefix + user_input + suffix
    result = {"Result":combined}
    return result


