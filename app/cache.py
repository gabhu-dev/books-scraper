from .scraper import get_books, get_categories

_cache = {}

def get_books_cached():
    if "books" not in _cache:
        _cache["books"] = get_books()
    return _cache["books"]

def get_categories_cached():
    if "categories" not in _cache:
        _cache["categories"] = get_categories()
    return _cache["categories"]