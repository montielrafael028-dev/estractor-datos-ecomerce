import csv
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"
cabeceras = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
print(f"Iniciando la extracion de datos...")

respuesta = requests.get(url, headers=cabeceras)
print(f"codigo de respuesta del servidor: {respuesta.status_code}")

soup = BeautifulSoup(respuesta.text, "html.parser")

libros = soup.find_all("article", class_="product_pod")

datos_libros = []

for libro in libros:
    Titulo = libro.h3.a["title"]
    Precio = libro.find("p", class_="price_color").text
    precio_limpio = Precio[1:]
    print(Titulo, precio_limpio)
    
    datos_libros.append({"Titulo": Titulo, "Precio": precio_limpio})
    
with open("reporte_libros.csv", mode="w", newline="", encoding="utf-8") as archivo:
    columnas = ["Titulo", "Precio"]
    escritor = csv.DictWriter(archivo, fieldnames=columnas)
    escritor.writeheader()
    escritor.writerows(datos_libros)
    
print("!Archivo CSV guardado con exito¡")