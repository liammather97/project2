from flask import Flask, redirect, url_for, request, jsonify
from application import app
import random
import json

suffix = [" the Great", " the Smelly", " the Rich", " the Cool",
" the Jeweller", " the Daddy", " the Snitch", " the Gangsta",
 " the Gunner", " the Dude", " the Thief", " the Original", " the Nerd"]

@app.route('/suffix', methods=['GET', 'POST'])
def suffix_gen():
    the_choice=random.choice(prefix)
    prefix1 = jsonify({"choice":the_choice})
    return prefix1


