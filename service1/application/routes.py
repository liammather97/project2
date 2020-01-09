from app import application
from flask import render_template
from application.forms import NameForm

@app.route('/', '/home')
def home():


@app.route('/generator', methods=['GET', 'POST'])
def gen():
    form = NameForm()
    if request.method == 'POST':
        return form.name

    return render_template('generator.html', title='Enter your name: ', form=form)

