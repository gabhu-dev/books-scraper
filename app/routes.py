from flask import Blueprint, render_template
from .cache import get_books_cached, get_categories_cached

main = Blueprint('main', __name__)

@main.route('/')
def index():
    categories = get_categories_cached()
    books = get_books_cached()
    return render_template('index.html', categories=categories, books=books)

@main.route('/details')
def details():
    return render_template('details.html')