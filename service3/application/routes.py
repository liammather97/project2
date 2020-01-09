from flask import Flask, redirect, url_for, request
from application import app
import random

suffix = [" the great", " the smelly", " the rich", " the cool",
" the jeweller", " the daddy", " the snitch", " the gangsta",
 " the gunner", " the dude"]

@app.route('/prefix', methods=['GET', 'POST'])
def suffix_gen():
    return(random.choice(suffix))