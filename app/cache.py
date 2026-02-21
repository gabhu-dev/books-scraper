from .scraper import get_books, get_categories, get_details

_cache = {}

def get_books_cached(url=None, search=None):
    # Asegurar que los parámetros vacíos se traten igual (None o "")
    url = url if url else None
    search = search if search else None
    
    cache_key = f"books_{url}_{search}"
    if cache_key not in _cache:
        # Pasamos los parámetros al scraper para que él haga el trabajo pesado
        _cache[cache_key] = get_books(url=url, search=search) if url else get_books(search=search)
        
    return _cache[cache_key]

def get_categories_cached():
    if "categories" not in _cache:
        _cache["categories"] = get_categories()
    return _cache["categories"]

def get_details_cached(url_detail):
    cache_key = f"detail_{url_detail}"
    if cache_key not in _cache:
        _cache[cache_key] = get_details(url_detail)
    return _cache[cache_key]