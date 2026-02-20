from flask import Blueprint, render_template
from .cache import get_books_cached, get_categories_cached

main = Blueprint('main', __name__)

@main.route('/')
def index():
    categories = get_categories_cached()
    books = get_books_cached()
    # book_test = [{
    #     "title": "A Light in the Attic",
    #     "price": "Â£51.77",
    #     "image_url": "https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg",
    #     "rating": 3,
    #     "url_detail": "catalogue/a-light-in-the-attic_1000/index.html"
    # }]
    # print('books', books)
    return render_template('index.html', categories=categories, books=books)

@main.route('/details')
def details():
    return render_template('details.html')