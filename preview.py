import requests
from bs4 import BeautifulSoup
import time

# Headers para simular un navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Leer los URLs previamente extraídos
with open("plantillas_urls.txt", "r", encoding="utf-8") as file:
    urls = [line.strip() for line in file.readlines()]  # Ahora ya tienes los URLs completos

# Inicializar una lista para almacenar los resultados
resultados = []

# Iterar sobre cada URL
for url in urls:
    try:
        # Realizar una solicitud GET para obtener el contenido de cada página de plantilla
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extraer el nombre de la plantilla desde el <h1>
            h1_tag = soup.find('h1')
            if h1_tag:
                nombre_plantilla = h1_tag.get_text().strip()
            else:
                nombre_plantilla = "Nombre no encontrado"

            # Buscar el enlace de vista previa desde las etiquetas <a> con las clases específicas
            preview_link = "Vista previa no encontrada"
            a_tag = soup.find('a', class_='nr9DhCl_ UbiTW8dm vGSJYVYs Mvefxhtu')
            if a_tag and 'href' in a_tag.attrs:
                preview_link = a_tag['href']

                # Imprimir el enlace de vista previa en la consola
                print(f"URL de vista previa: {preview_link}")

            # Almacenar el resultado en la lista
            resultados.append((nombre_plantilla, url, preview_link))

            # Agregar una pausa entre solicitudes para no sobrecargar el servidor (buena práctica)
            time.sleep(1)
        else:
            print(f"Error al acceder a {url}. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error al procesar {url}: {str(e)}")

# Guardar los resultados en un archivo
with open("plantillas_completas.txt", "w", encoding="utf-8") as file:
    for nombre, plantilla_url, preview_url in resultados:
        file.write(f"Nombre de la plantilla: {nombre}\n")
        file.write(f"URL de la plantilla: {plantilla_url}\n")
        file.write(f"Enlace de vista previa: {preview_url}\n\n")

print(f"Proceso completado. Los resultados se han guardado en 'plantillas_completas.txt'.")
