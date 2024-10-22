import requests

# API Key de Google Cloud
API_KEY = 'AIzaSyCJInl7NQUgMHD7sLL7ML57LAjYUTKbqyI'

# URL de PageSpeed Insights API
API_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

# Función para obtener los puntajes de PageSpeed Insights
def get_pagespeed_data(url, strategy="desktop"):
    # Parámetros de la solicitud
    params = {
        'url': url,
        'key': API_KEY,
        'category': ['performance', 'accessibility', 'best-practices', 'seo'],
        'strategy': strategy  # Añadir estrategia para escritorio o móvil
    }
    
    # Realizar la solicitud a la API
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Obtener los puntajes de cada categoría (si existen)
        performance_score = data.get('lighthouseResult', {}).get('categories', {}).get('performance', {}).get('score', 0) * 100
        accessibility_score = data.get('lighthouseResult', {}).get('categories', {}).get('accessibility', {}).get('score', 0) * 100
        best_practices_score = data.get('lighthouseResult', {}).get('categories', {}).get('best-practices', {}).get('score', 0) * 100
        seo_score = data.get('lighthouseResult', {}).get('categories', {}).get('seo', {}).get('score', 0) * 100
        
        # Imprimir los resultados
        print(f"Resultados para {url} ({'Móvil' if strategy == 'mobile' else 'Escritorio'}):")
        print(f"Rendimiento: {performance_score:.1f}")
        print(f"Accesibilidad: {accessibility_score:.1f}")
        print(f"Mejores prácticas: {best_practices_score:.1f}")
        print(f"SEO: {seo_score:.1f}")
    else:
        print(f"Error al acceder a la API. Código de estado: {response.status_code}")

# Ingresar la URL que deseas analizar
url = input("Introduce la URL que deseas analizar: ")

# Llamar a la función para obtener y mostrar los puntajes para escritorio
get_pagespeed_data(url, strategy="desktop")

# Llamar a la función para obtener y mostrar los puntajes para móvil
get_pagespeed_data(url, strategy="mobile")
