from flask import Flask, request, jsonify
from scraping import scrape_data
from textProcessor import process_text
import sqlite3

app = Flask(__name__)

# Endpoint para hacer web scraping
@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    data = scrape_data(url)
    
    # Guardar el resultado en la base de datos
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scraped_data (url, title, description) VALUES (?, ?, ?)",
                   (url, data['title'], data['description']))
    conn.commit()
    conn.close()

    return jsonify(data)

# Endpoint para procesar texto con un modelo de Hugging Face
@app.route('/process', methods=['POST'])
def process():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'Text is required'}), 400

    result = process_text(text)

    # Guardar el resultado en la base de datos
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO processed_text (text, summary) VALUES (?, ?)",
                   (text, result['summary']))
    conn.commit()
    conn.close()

    return jsonify(result)

# Endpoint para combinar scrape y procesamiento de texto
@app.route('/combined', methods=['POST'])
def combined():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Realizar el scraping de datos
    scraped_data = scrape_data(url)
    
    # Procesar el texto (obtener un resumen)
    summary_result = process_text(scraped_data['description'])

    # Guardar ambos resultados en la base de datos
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO combined_results (url, title, description, summary) VALUES (?, ?, ?, ?)",
                   (url, scraped_data['title'], scraped_data['description'], summary_result['summary']))
    conn.commit()
    conn.close()

    return jsonify({
        'scraped_data': scraped_data,
        'summary_result': summary_result
    })

if __name__ == '__main__':
    app.run(debug=True)