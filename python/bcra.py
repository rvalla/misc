import requests

data = requests.get("https://api.bcra.gob.ar/estadisticas/v3.0/Monetarias", verify=False).json()
print(data)


  
  
   
