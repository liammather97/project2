from application import app
from flask import render_template, request
from application.forms import NameForm

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/generator', methods=['GET', 'POST'])
def generator():
    form = NameForm()
    if request.method == 'POST':
        return form.name.data

    return render_template('generator.html', title='Generator', form=form)

