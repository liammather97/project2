from flask import Flask, redirect, url_for, request
from application import app
import random

suffix = [" the Great", " the Smelly", " the Rich", " The cool",
" the Jeweller", " the Daddy", " the Snitch", " the Gangsta",
 " the Gunner", " the Dude"]

@app.route('/suffix', methods=['GET', 'POST'])
def suffix_gen():
    return(random.choice(suffix))