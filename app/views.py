from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname' : 'Seth' }
	return render_template('index.html', title='Home', user=user);


@app.route('/scanner')
def scanner():
	return render_template('scanner.html');

@app.route('/scanner2')
def scanner2():
	return render_template('scanner2.html')
