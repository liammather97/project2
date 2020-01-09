from flask import Flask, redirect, url_for, request
from application import app
import random

prefix = ["yung ", "lil ", "big ", "tall ",
"short ", "chief ", "sir ", "lord ", "slick ",
 "fat ", "skinny "]

@app.route('/prefix', methods=['GET', 'POST'])
def prefix_gen():
    return(random.choice(prefix))
