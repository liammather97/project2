from flask import Flask, redirect, url_for, request
from application import app
import random

prefix = ["Yung ", "Lil ", "Big ", "Tall ",
"Short ", "Chief ", "Sir ", "Lord ", "Slick ",
 "Fat ", "Skinny ", "Icy ", "Spooky ", "Clever " "Colonel "]

@app.route('/prefix', methods=['GET', 'POST'])
def prefix_gen():
    prefix1 = (random.choice(prefix))
    return prefix1