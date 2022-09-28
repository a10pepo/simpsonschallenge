import requests
import time

x = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')


img_data = requests.get(x.json()[0]["image"]).content
with open('imagen.jpg', 'wb') as handler:
    handler.write(img_data)

print(x.json())

while True:
    time.sleep(60)