import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
BASE_URL_INDEX = BASE_URL + "index.html"

RATING_MAP = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}

def get_categories():
    print('Obteniendo categorías...')
    response = requests.get(BASE_URL_INDEX)
    soup = BeautifulSoup(response.text, "html.parser")
    categories = []
    for li in soup.select(".side_categories ul li ul li a"):
        print(f'Categoría encontrada: {li.text.strip()}')
        categories.append({
            "category": li.text.strip(),
            "url": BASE_URL_INDEX + li["href"]
        })
    return categories

def get_books(url=BASE_URL_INDEX, search=None):
    print(f'Obteniendo libros desde: {url}')
    books = []
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for book in soup.select("article.product_pod"):
            title = book.h3.a["title"]
            price = book.select_one(".price_color").text.replace("Â£", "$")
            image_url = book.select_one('.image_container img')['src'].replace("../", "")
            rating_class = book.p["class"][1]
            rating = RATING_MAP.get(rating_class, 0)
            url_detail = book.h3.a["href"].replace("../", "")

            # Si el url_detail ya viene con "catalogue/" no lo dupliques
            if not url_detail.startswith("catalogue/"):
                url_detail = "catalogue/" + url_detail

            books.append({
                "title": title,
                "price": price,
                'image_url': BASE_URL + image_url,
                "rating": rating,
                "url_detail": url_detail
            })

        # Paginación
        next_btn = soup.select_one("li.next a")
        if next_btn:
            # Construir la URL de la siguiente página correctamente
            current_base = url.rsplit("/", 1)[0] + "/"
            url = current_base + next_btn["href"]
        else:
            url = None

    # Filtrar por búsqueda si existe
    if search:
        books = [book for book in books if search.lower() in book["title"].lower()]
    
    return books

def get_details(url_detail):
    url = BASE_URL + url_detail
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.select_one(".product_main h1").text
    price = soup.select_one(".price_color").text.strip()
    availability = soup.select_one(".availability").text.strip()
    description = soup.select_one("#product_description + p")
    description = description.text.strip() if description else "Sin descripción."
    rating_class = soup.select_one(".star-rating")["class"][1]
    rating = RATING_MAP.get(rating_class, 0)

    image_url = soup.select_one(".item.active img")["src"].replace("../../", "")
    
    return {
        "title": title,
        "price": price,
        "availability": availability,
        "description": description,
        "rating": rating,
        "image_url": BASE_URL + image_url
    }