from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    name = 'gabriela'
    return render_template('index.html', name=name)

@main.route('/details')
def details():
    return render_template('details.html')