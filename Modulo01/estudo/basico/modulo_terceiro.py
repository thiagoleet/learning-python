# pip install requests==2.31.0
import requests

print("\nImportação e uso de módulo de terceiros")

url = "http://www.google.com"
response = requests.get(url)
print(
    f"Solicitação para url {url} retornou o status code: {response.status_code}")
