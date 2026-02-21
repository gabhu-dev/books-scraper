from .scraper import get_books, get_categories, get_details

_cache = {}

def get_books_cached():
    if "books" not in _cache:
        _cache["books"] = get_books()
    return _cache["books"]

def get_categories_cached():
    if "categories" not in _cache:
        _cache["categories"] = get_categories()
    return _cache["categories"]

def get_details_cached(url_detail):
    cache_key = f"detail_{url_detail}"
    if cache_key not in _cache:
        _cache[cache_key] = get_details(url_detail)
    return _cache[cache_key]