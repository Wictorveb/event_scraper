# Este archivo solo descarga la web; regla de oro, un archivo = una responsabilidad
import requests # Importamos la libreria que sabe: hacer peticiones a la web y manejar respuestas HTTP

def download_page(url: str) -> str: # url: str es la direccion web y -> str devuelve texto (HTML); estoi es lo que documenta la funcion
    # Descarga una página web y develve su html como texto

    response = requests.get(url) # Conecta a la web, envia una peticon http get, espera la respuesta

    # Si la web no responde correctamente, lanzamos el error
    response.raise_for_status

    return response.text # Esto es el html completo como un str

def save_html(html: str, path: str):
    # Guarda el HTML en un archivo local
    with open(path, "w", encoding="utf8") as f: # "w" es escribir y "utf8 hace que se permitan caracteres especiales como tildes"
        f.write(html) # Guarda el HTML tal cual, sin tocarlo