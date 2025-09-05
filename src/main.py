# Este script utiliza la librería 'requests' para hacer una solicitud HTTP
# y demostrar que las dependencias se instalaron correctamente.

import requests
import sys

print("Iniciando la ejecución del script...")

try:
    # URL de prueba actualizada a Google
    url = "https://www.google.com"
    response = requests.get(url)
    
    # Imprime el código de estado para verificar que la solicitud fue exitosa
    print(f"La solicitud a la URL {url} ha terminado con el código de estado: {response.status_code}")
    
    # Verifica que el código de estado es 200 (OK)
    if response.status_code == 200:
        print("¡El script se ha ejecutado con éxito y la solicitud fue exitosa!")
    else:
        print(f"Error: La solicitud falló con el código de estado {response.status_code}")
        sys.exit(1)

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al intentar hacer la solicitud: {e}")
    sys.exit(1)

print("Ejecución del script finalizada.")