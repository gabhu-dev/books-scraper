from flask import Blueprint, render_template, request
from .cache import get_books_cached, get_categories_cached, get_details_cached

main = Blueprint('main', __name__)

@main.route('/')
def index():
    query = request.args.get('q')
    category_url = request.args.get('category')
    
    categories = get_categories_cached()
    # Si no hay categoría seleccionada, usamos la por defecto (index)
    books = get_books_cached(url=category_url, search=query)
    return render_template('index.html', categories=categories, books=books)

@main.route('/book/<path:url_detail>')
def book_details(url_detail):
    book = get_details_cached(url_detail)
    return render_template('details.html', book=book)