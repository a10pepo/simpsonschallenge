import time
import csv
import requests
import os
import string


#Difinición de la función que obtiene datos del API
def obtenerPerso():
  URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'
  respuesta = requests.get(url=URL)
  datos = respuesta.json()
  # Obtenemos valor en la clave 'character' del JSON que nos interesa
  dic: str = datos[0]
  return dic

#Función que borra el contenido de un csv
def csv_borrar_datos():
    file = open("Contador.csv", "w")
    file.close()

contadorPalabras:dict = {}
#Bucle que guarda los datos en el csv según el personaje
while True:
  #Obtenemos todos los datos que nos devuelve la API
  try:
    datos = obtenerPerso()
    print(datos)
  except:
    print("Error in the request")
  if len(datos)>0:
    #creamos el diccionario con lo que queremos añadir al CSV
    my_dict = {'quote': datos['quote']}
    #Nos guardamos el autor para poder clasificarlo
    autor = datos['character']
    autor=autor.replace("'","").replace(" ","_")
    #Sacamos los datos de la imagen
    urlImag = datos["image"]
    #Cogemos el contenido de la url de la API
    imagen = requests.get(urlImag).content
    #Creamos el nombre de la imagen a guardar
    nombreImagen = str(autor) + ".png"

    try:
        open('/datafolder/Contador.csv', 'a').close()
        os.mkdir(f'/datafolder/{str(autor)}')
    except:
        print("Character already exists, append")

    
        
    rutaCSV =  '/datafolder/' + str(autor) + "/" + str(autor) + ".csv"
    rutaImagen =  '/datafolder/' + str(autor) + "/" + str(autor) + ".png"

    
    #Creamos el diccionario que contiene el conteo de cada palabra que vamos leyendo
    valor = my_dict['quote']
    spl = str(valor).split()
    for e in spl:
        #Quitamos signos de puntuación de nuestro texto
        e = e.translate(str.maketrans('', '', string.punctuation))
        #Nos preguntamos si ya existe esa palabra en el diccionario
        if e in contadorPalabras:
            n = contadorPalabras[e]
            contadorPalabras[e] = n+1
        #Si no existe en el diccionario lo añadimos por primera vez
        else:
            contadorPalabras[e] = 1

    print(contadorPalabras)

    #Borramos el contenido del csv
    csv_borrar_datos()
    #Escribimos el diccionario de lapalbra en un csv
    with open('/datafolder/Contador.csv', 'a+') as f:  
        writer = csv.writer(f)
        for k, v in contadorPalabras.items():
            writer.writerow([k, v])

    #Creación de los csv de cada personaje que leemos y descargamos su imagen 
    try:
        with open(rutaCSV, 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel', lineterminator=';')
            wr.writerow(my_dict.values())
        with open(rutaImagen, 'wb') as handler:
            handler.write(imagen)
    except FileNotFoundError:
        os.mkdir('datafolder/' + str(autor))
        with open(rutaCSV, 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel', lineterminator=';')
            wr.writerow(my_dict.values())
        with open(rutaImagen, 'wb') as handler:
            handler.write(imagen)
    
    print(f"Found {autor} and {my_dict}")
  else:
    print("Error retrieving data")
  time.sleep(30)