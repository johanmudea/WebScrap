from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos

eq = soup.find_all("span", class_="nombre-equipo")

equipos = list()

count = 0


for i in eq:

    if count <20:

       equipos.append(i.text)

    else:
         break

    count+=1

print(equipos)

#Puntaje

pt = soup.find_all("td", class_="destacado")

puntaje = list()


count = 0

for i in pt:

    if count <20:

         puntaje.append(i.text)

    else:
        break

    count+=1

print(puntaje)


df = pd.DataFrame({"Nombre": equipos, "puntos": puntaje}, index = list(range(1, 21)))

print(df)

df.to_csv("Clasificacion.csv", index = False)
