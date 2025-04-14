import requests
from PIL import Image
from io import BytesIO

# Configurações do WMS
geoserver_url = "http://localhost:8080/geoserver/meu_workspace/wms"
params = {
    "service": "WMS",
    "version": "1.1.1",
    "request": "GetMap",
    "layers": "meu_workspace:municipios_pb",
    "styles": "",
    "bbox": "-35.92,-7.02,-35.84,-6.95",  # Coordenadas aproximadas de Esperança/PB
    "width": "800",
    "height": "600",
    "srs": "EPSG:4674",
    "format": "image/png"
}

# Requisição ao GeoServer
response = requests.get(geoserver_url, params=params)

# Exibir a imagem
if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    image.show()
else:
    print("Erro ao obter a imagem:", response.status_code)
