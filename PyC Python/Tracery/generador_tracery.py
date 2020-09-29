
# Importamos la libreria de tracery y algunas funciones del idioma Ingles
# Tambien importamos la libreria de tiempo de python
import tracery
import time
from tracery.modifiers import base_english

# Tracery es una libreria que permite generar textos de forma sencilla, y aun asi lograr estructuras complejas
# Para usarla definiremos las reglas de juego

# Primero definiremos los grupos tematicos ,estos se pueden construir de varias maneras

# listas
lista_de_objetos = ['reloj', 'piano', 'pescado', 'avion','lapiz','perro','machete','helado','taladro','borrador']

# lista de emojis en unicode

# en esta pagina encontraran la mayoria de emojis https://unicode.org/emoji/charts/full-emoji-list.html
# el formato para los emoticones en unicode debe ser '\U' + '8 caracteres'
# en caso que el emoticon tenga mas de un linea se deben juntar
# U+1F600 seria \U0001F600 , como tiene 5 caracteres se llenaria con 3 ceros
# U+2601 seria \U00002601 , como tiene 4 caracteres se llenaria con 4 ceros
# U+1F468 U+200D U+1F467 seria \U0001F468\U0000200D\U0001F467

emojis = ['\U00002601','\U0001F468\U0000200D\U0001F467','\U0001f618','\U0001f629','\U0001F642']


# archivos de texto , las palabras se almacenaran como una lista en la variable 'lista_de_formas'
# la 'r' significa 'read' de solo lectura y preferiblemente el archivo debe estar en la misma carpeta del programa

with open('lugares.txt','r') as texto_de_formas:
    lista_de_lugares = texto_de_formas.read().splitlines()

# aca uniremos todas las posibles combinaciones de palabras ademas de la estructura del mensaje

reglas = {
    # Primero definimos la estructura de la frase , entre # estan los grupos de palabras
    # En este caso usaremos el modificador .capitalize para hacer que la primera palabra tenga la primera letra en mayuscula
    'estructura_final': 'el #dia.capitalize# es como un #objeto# que #estado_y_lugar# #emojis#',
        # Seguimos con el contenido, aca podemos crear los grupos de palabras a usar y agruparlas dentro de una variable
        # O tambien podemos vincular las listas creadas arriba
    'dia': ['lunes','martes','miercoles','jueves','viernes','sabado','domingo'],
    'objeto': lista_de_objetos,
        # Podemos agregar estructuras dentro de otras, en este caso #estado_y_lugar# contiene una estructura interna
    'estado_y_lugar': '#estado# en un #lugar#',
    'estado': ['tambalea','dibuja','llora','sonrie','rie','espera','escupe','flota'],
    'lugar': lista_de_lugares,
    'emojis': emojis}


# Tracery sirve con 'grammars'  que se definen como un diccionario de simbolos
# Aca estamos creando un 'grammar' con nuestras reglas y asignandolo a la variable 'gramatica'
grammar = tracery.Grammar(reglas)
# add.modifiers añade modificadores como el '.capitalize' en la estructura final
grammar.add_modifiers(base_english)
# '.flatten' convierte el 'grammar' en texto
grammar.flatten("que le puedo decir... #estructura_final#")


# Pueden descomentar este codigo para que imprima una frase cada 3 segundos
'''
while True:
    variable = texto_final()
    print(variable)
    time.sleep(3)
'''
resultado = texto_final()
print(resultado)
