# html, css y JavaScript

# estructura de contenido, diseño y estilo, elementos interactivos

# pip install beautifulsoup4
# pip install lxml
# pip install requests

# Ver el codigo fuente

import bs4
import requests # busqueda

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

print(type(resultado))
#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
#print(sopa)

print(sopa.select('title'))
print(sopa.select('title')[0]) # indice
print(sopa.select('title')[0].getText())
print(sopa.select('h1'))

parrafo_especial = sopa.select('p')

# '' soup.select('div') Todos los elementos con la etiqueta 'div'
#  # soup.select('#estilo') Elemento que contengan id = 'estilo'
# . ''' elementos que contengan class

columna_lateral = sopa.select('.content p')

for p in columna_lateral:
    print(p.getText())

#imagenes = sopa.select('.course-box-image')[0]['src']

imagenes = sopa.select('img')

imagen_curso_1 = requests.get(imagenes)
#print(imagen_curso_1.content)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()

# https://books.toscrape.com/




