import requests

data = requests.get("https://api.bcra.gob.ar/estadisticas/v2.0/datosvariable/31/2024-08-31/2024-08-31", verify=False).json()
print(data["results"])

