import requests
from bs4 import BeautifulSoup

# Headers para simular un navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Prefijo de la URL principal que deseas analizar (sin la parte de la página)
base_url = "https://elements.envato.com/es/wordpress/marketing+digital/pg-"

# Archivo donde se guardarán las URLs de las plantillas
output_file = "plantillas_urls.txt"

# Inicializar una lista para almacenar los URLs
all_urls = []

# Iterar a través de las páginas de 1 a 5
for page_num in range(1, 6):
    # Construir la URL para la página actual
    url = f"{base_url}{page_num}"
    
    # Realizar la petición HTTP para obtener el contenido de la página
    response = requests.get(url, headers=headers)

    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar todos los divs con clase 'bAub8HEX'
        for main_div in soup.find_all('div', class_='bAub8HEX'):
            # Dentro de este div, encontrar los divs con clase 'wtigj7JD'
            inner_div = main_div.find('div', class_='wtigj7JD')

            if inner_div:
                # Dentro de este div, encontrar la etiqueta <a> y extraer el href
                a_tag = inner_div.find('a')
                if a_tag and 'href' in a_tag.attrs:
                    # Añadir la URL completa al prefijo base
                    full_url = "https://elements.envato.com" + a_tag['href']
                    all_urls.append(full_url)

        print(f"Página {page_num} procesada. Se han encontrado {len(all_urls)} URLs hasta ahora.")

    else:
        print(f"Error al acceder a la página {page_num}. Código de estado: {response.status_code}")

# Guardar todas las URLs extraídas en el archivo, sobrescribiendo el archivo anterior
with open(output_file, "w", encoding="utf-8") as file:
    for url in all_urls:
        file.write(f"{url}\n")

print(f"Proceso completado. Se han guardado {len(all_urls)} URLs en '{output_file}'.")
