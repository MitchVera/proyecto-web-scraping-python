from transformers import pipeline

# Cargar el modelo de resumen
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def process_text(text):
    # Generar resumen del texto
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return {'summary': summary[0]['summary_text']}