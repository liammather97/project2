from flask import Flask, redirect, url_for, request, jsonify
from application import app
import random
import json

prefix = ["Yung ", "Lil ", "Big ", "Tall ",
"Short ", "Chief ", "Sir ", "Lord ", "Slick ",
 "Fat ", "Skinny ", "Icy ", "Spooky ", "Clever " "Colonel "]

@app.route('/prefix', methods=['GET', 'POST'])
def prefix_gen():
    the_choice=random.choice(prefix)
    prefix1 = jsonify({"choice":the_choice})
    return prefix1
