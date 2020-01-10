from flask import Flask, redirect, url_for, request
from application import app
import random

suffix = [" the Great", " the Smelly", " the Rich", " the Cool",
" the Jeweller", " the Daddy", " the Snitch", " the Gangsta",
 " the Gunner", " the Dude", " the Thief", " the Original", " the Nerd"]

@app.route('/suffix', methods=['GET', 'POST'])
def suffix_gen():
    suffix1 = {"choice":random.choice(suffix)}
    return suffix1