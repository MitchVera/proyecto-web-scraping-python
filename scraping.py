import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Obtener el título de la página
    title = soup.find('h1').text if soup.find('h1') else 'No title found'

    # Obtener todos los párrafos <p> de la página
    paragraphs = soup.find_all('p')  # Encuentra todos los <p>

    # Filtrar párrafos que contienen texto y cuya longitud sea mayor que el título
    matching_paragraphs = [
        p.text.strip() for p in paragraphs
        if p.text.strip() and len(p.text.strip()) > len(title) and '\n' not in p.text
    ]

    # Si hay párrafos que cumplen la condición, retorna el primero, de lo contrario, retorna un mensaje predeterminado
    description = matching_paragraphs[0] if matching_paragraphs else 'No description found'

    # Retornar el título y la descripción
    return {'title': title, 'description': description}