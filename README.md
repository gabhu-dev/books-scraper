# Books Scraper 📚

**Link de la demo:** [https://books-scraper.onrender.com/](https://books-scraper.onrender.com/)

Este proyecto es una aplicación web desarrollada con **Flask** que realiza scraping en tiempo real del sitio [Books to Scrape](https://books.toscrape.com/), una plataforma diseñada específicamente para practicar técnicas de extracción de datos.

## 🚀 De qué trata el proyecto
La aplicación permite explorar un catálogo de libros extraído directamente del sitio fuente. Los usuarios pueden navegar por categorías, buscar libros específicos por título y ver detalles individuales de cada obra, todo a través de una interfaz moderna y responsiva.

## ✨ Funciones principales
- **Scraping Dinámico**: Extrae títulos, precios, ratings e imágenes directamente de la fuente.
- **Navegación por Categorías**: Filtra el catálogo según las categorías disponibles en el sitio original.
- **Búsqueda**: Permite buscar libros por palabras clave en el título.
- **Vista de Detalles**: Información extendida de cada libro (descripción, disponibilidad, etc.).
- **Sistema de Caché**: Implementa una caché interna para evitar peticiones redundantes y mejorar la velocidad de carga.
- **Optimización de Scraping**: El scraper está limitado a procesar las primeras 2 páginas para garantizar tiempos de respuesta rápidos y evitar bloqueos o timeouts en despliegues cloud.

## 🛠️ Tecnologías y Librerías
- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)
- **Scraping**: [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) y [Requests](https://requests.readthedocs.io/)
- **Frontend**: [Tailwind CSS](https://tailwindcss.com/)
- **Iconografía**: [Lucide Icons](https://lucide.dev/)
- **Otras**: Jinja2 (Motores de plantillas de Flask)

## 📦 Instalación y Uso

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd books-scraper
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   # En Windows
   python -m venv venv
   .\venv\Scripts\activate

   # En Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```bash
   python run.py
   ```
   La aplicación estará disponible en `http://localhost:5000`.

---
*Aviso: Este proyecto tiene fines educativos. El scraping se realiza sobre https://books.toscrape.com/, un sitio creado para este propósito específico.*
