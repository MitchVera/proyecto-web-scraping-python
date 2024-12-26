# Proyecto Web Scraping con Python

Este proyecto es una aplicación web que utiliza Flask para realizar scraping de sitios web y análisis de texto. A continuación, se detallan las instrucciones para ejecutar el proyecto y utilizar sus funcionalidades.

## Instrucciones para ejecutar el proyecto


1. **Crear un Entorno Virtual**:
   - Es una buena práctica usar un entorno virtual para gestionar las dependencias de los proyectos de manera separada.
   - Se crea un entorno virtual ejecutando el siguiente comando:

 python -m venv venv

2. **Activar el Entorno Virtual**:
   - En Windows:

 	venv\Scripts\activate


- En macOS/Linux:

	source venv/bin/activate

3. **Instalar las dependencias**: Se ejecutan los siguientes comandos para instalar las dependencias necesarias:

-pip install Flask

-pip install beautifulsoup4

-pip install requests

-pip install Transformers

-pip install torch


4. **Ejecutar la base de datos**: 
   - El archivo `db.sqlite` es el archivo de base de datos.
   - Si el archivo de datos no está presente, se ejecuta el siguiente comando en el directorio del proyecto para crear una nueva base de datos con las columnas respectivas:

	python db_setup.py


5. **Ejecutar el servidor Flask**: 
   - Se navega al directorio del proyecto y se ejecuta el siguiente comando:

	python app.py

   - El servidor estará disponible en [http://127.0.0.1:5000](http://127.0.0.1:5000).

6. **Endpoints**:
   - **POST /scrape**: Para extraer titulares y descripciones de una URL.
   - **POST /process**: Para procesar un texto y obtener el análisis de sentimiento.
   - **POST /combined**: Para combinar el scraping y procesamiento en un solo paso.

7. **Pruebas**: Las pruebas se realizaron con Postman. Aquí algunos ejemplos de solicitudes:
   - **Solicitud POST a /scrape**:

json { "url": "https://www.t13.cl/noticia/politica/declaraciones-jefe-gabinete-funcionarios-del-hotel-panamericano-dan-cuenta-mons-24-12-2024" }

- **Solicitud POST a /combined**:

json { "url": "https://www.t13.cl/noticia/politica/declaraciones-jefe-gabinete-funcionarios-del-hotel-panamericano-dan-cuenta-mons-24-12-2024" }

- **Solicitud POST a /process**:

json { "text": "Valparaíso es una comuna y ciudad capital de la provincia y Región de Valparaíso. Se sitúa en la zona central de Chile y es el centro histórico, institucional y universitario del Gran Valparaíso, que forma junto a los municipios de Viña del Mar, Quilpué, Villa Alemana y Concón. Como capital de la región, alberga a la Delegación Presidencial y al Gobierno Regional de Valparaíso, además de ser sede del Congreso Nacional, un importante terminal portuario y una de las tres urbes chilenas más pobladas." }


8. **Consideraciones**: 
   - **Versión de Python**: 3.11.4

## Lista de artículos de prueba

- [Artículo 1](https://www.t13.cl/noticia/politica/declaraciones-jefe-gabinete-funcionarios-del-hotel-panamericano-dan-cuenta-mons-24-12-2024)
- [Artículo 2](https://www.latercera.com/nacional/noticia/tacos-esperas-y-semaforos-sin-funcionar-marcan-intervencion-de-plaza-italia-por-proyecto-nueva-alameda/XC4BUFMYMZBJ3O37XGDTQI2IK4/#)
- [Artículo 3](https://www.publimetro.cl/noticias/2024/12/25/cuerpo-de-bomberos-de-los-angeles-suspende-a-comandante-acusado-del-delito-de-usurpacion-de-agua/)
- [Artículo 4](https://www.df.cl/empresas/industria/chile-light-departamento-de-agricultura-de-eeuu-ve-notable-cambio)

