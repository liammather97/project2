from flask import Flask, redirect, url_for, request
from application import app
import random

prefix = ["Yung ", "Lil ", "Big ", "Tall ",
"Short ", "Chief ", "Sir ", "Lord ", "Slick ",
 "Fat ", "Skinny "]

@app.route('/prefix', methods=['GET', 'POST'])
def prefix_gen():
    return (random.choice(prefix))