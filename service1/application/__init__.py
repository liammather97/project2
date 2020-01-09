from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bigfatsecret'

from application import routes