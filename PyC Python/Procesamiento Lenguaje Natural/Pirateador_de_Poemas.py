
import spacy
import random
random.seed()
# función auxiliar
def leer_texto(texto):
    """Funcion auxiliar para leer un archivo de texto"""
    with open(texto, 'r' , encoding="latin-1") as text:
        
        return text.read()

#,encoding='latin-1'
nlp = spacy.load('es_core_news_lg')
doc = nlp("Yo la verdad sí extraño mi primer trabajo serio con el que pagué mi primera carrera porque era en una aseguradora, horario de oficina, comisionaba muy bien y la verdad ganaba más que lo que ahora gano.")


texto = leer_texto("Sirena.txt")
texto_procesado = nlp(texto)
poema = leer_texto("p1.txt").encode("latin-1").decode("utf-8")
poema_procesado = nlp(poema)


resultado = ""
for tokenpoema in poema_procesado:
    #print(tokenpoema.tag_[0:3])
    if tokenpoema.tag_[0:3] == "NOU" or tokenpoema.tag_[0:3] == "ADJ":
        resultado = f"{resultado} {random.choice([token.orth_ for token in texto_procesado if token.tag_ == tokenpoema.tag_])} "
    else:
        resultado = f"{resultado} {tokenpoema.text}"

print(resultado)


"""
file1 = open("resultado1 poema2.txt","w",encoding="latin-1") 
file1.write(resultado)
file1.close
"""

