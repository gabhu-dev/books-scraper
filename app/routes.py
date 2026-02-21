from flask import Blueprint, render_template
from .cache import get_books_cached, get_categories_cached, get_details_cached

main = Blueprint('main', __name__)

@main.route('/')
def index():
    categories = get_categories_cached()
    books = get_books_cached()
    return render_template('index.html', categories=categories, books=books)

@main.route('/book/<path:url_detail>')
def book_details(url_detail):
    book = get_details_cached(url_detail)
    return render_template('details.html', book=book)