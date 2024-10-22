import re

# Ruta del archivo con la información completa
archivo_completo = "plantillas_completas.txt"

# Ruta del archivo donde se guardarán los enlaces de vista previa
archivo_urls = "urls_limpias.txt"

# Expresión regular para extraer las URLs de vista previa
regex_url_preview = r"Enlace de vista previa:\s*(https?://[^\s]+)"

# Inicializar una lista para almacenar las URLs de vista previa
urls_preview = []

# Leer el archivo y extraer las URLs de vista previa
with open(archivo_completo, "r", encoding="utf-8") as file:
    contenido = file.read()

    # Buscar todas las coincidencias de la expresión regular
    urls_preview = re.findall(regex_url_preview, contenido)

# Guardar las URLs en el nuevo archivo
with open(archivo_urls, "w", encoding="utf-8") as file:
    for url in urls_preview:
        file.write(f"{url}\n")

print(f"Proceso completado. Las URLs de vista previa se han guardado en '{archivo_urls}'.")
