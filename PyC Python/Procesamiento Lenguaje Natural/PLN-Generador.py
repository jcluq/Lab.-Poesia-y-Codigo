#____ Generador de frases con PLN y tokens________________________
#Antes de comenzar, asegurate de instalar el corpus.
#Abrir la consola y escribe: 
# 
#
#python -m spacy download es_core_news_md 
#                   o
#python -m spacy download es_core_news_lg
#
#
#El programa esta basado en la libreria de procesamiento de lenguaje natural Spacy
# https://spacy.io/usage



import spacy   #importamos spacy
import random  #importamos random 
from spacy.tokens import Doc
from spacy.vocab import Vocab


    # función auxiliar para abrir un documento .txt y leer el texto contenido en este
def leer_texto(texto):
    """Funcion auxiliar para leer un archivo de texto"""
    with open(texto, 'r',encoding="latin-1") as text:
        return text.read()

    #creamos nuestro <procesador> con la funcion spacy.load y pasamos el nombre de nuestro corpus como parametro, !!!!procesador es un metodo!!!!!
#procesador = spacy.load('es_core_news_lg')

    #usamos el metodo leer_texto(), y asignamos el nombre del archivo que deseamos procesar, 
    #el string resultante lo guardamos en la variable <texto>

#texto = leer_texto("Sirena.txt")    
    #usamos nuestro procesador y le asignamos el texto 
texto_procesado = Doc(Vocab()).from_disk("texto_procesado")    
#texto_procesado.to_disk("texto_procesado")
##procesador.to_disk("procesador")

    #Ahora tenemos un objeto llamado texto_procesado, el cual le ha asignado a cada palabra del texto una [tokenizacion]
    #Podemos valernos de una palabra aleatoria incluida en el tipo [tag] de cada token.
    #usamos la siguiente formula para crear el metodo correspondiente:
"""
            def NOMBRE_METODO():
                return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'TIPO DE TAG'])
"""
    #NOMBRE_METODO = al nombre que queramos asignar para la palabra
    #TIPO DE TAG = Un tag que describa el tipo de palabra
    # la lista: de tipos :  


def sustantivo_plural():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'NOUN__Gender=Masc|Number=Plur'])

def adjetivo_plural():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'ADJ__Gender=Masc|Number=Plur'])

def sust_sing_fem():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'NOUN__Gender=Fem|Number=Sing'])  

def adj_sing_fem():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'ADJ__Gender=Fem|Number=Sing'])  

def adverbio():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'ADV'])

def aux_plural_futuro():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'AUX__Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin'])


"""
def det_masc():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'DET__Definite=Def|Gender=Masc|Number=Plur'])

def det_fem():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'DET__Definite=Def|Gender=Fem|Number=Sing]'])

"""


for x in range(4):

    print(f'Los {sustantivo_plural()} {adjetivo_plural()}')
    print(f'{adverbio()} seran')
    print(f'La {sust_sing_fem()} {adj_sing_fem()}')

