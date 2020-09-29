#_____Wikibot___________________________________________________________________________________________________________________
#
# Esta es una pequena herramienta de extraccion de texto de wikipedia.
# Su funcionamiento esta basado en la libreria de python "wikipedia", la cual nos permite utilizar el api de wikipedia
# la documentacion completa de esta libreria se puede encontrar aqui: 
# https://wikipedia.readthedocs.io/en/latest/code.html#api -> Documentacion Oficial
# https://unipython.com/como-usar-la-libreria-wikipedia-de-python/ -> Recurso en Espanol
#






import wikipedia            #importamos la libreria, cuando utilicemos metodos de esta libreria, los llamaremos al objeto <wikipedia>

wikipedia.set_lang("es")    #definimos el lenguaje a usar con el metodo set_lang() y pasamos el parametro "es" para definir el espanol como lenguaje. 
contador = 0                #creamos una variable llamada <contador> para llevar la cuenta de las frases.
lineas = 10             #creamos una variable llamada <lineas> para definir cuantas veces se realizara el proceso.




while contador < lineas:    #Creamos un bucle que se repita hasta que la variable <contador> sea mayor que <lineas>

        # Usamos el metodo .random() para obtener un string con un nombre de un articulo aleatorio de wikipedia, 
        # y lo asignamos a la variable <articulo>
    articulo =  wikipedia.random()    
    #print(articulo)
        # Usamos el metodo .page() y pasamos nuestra variable de <articulo> para obtener un objeto tipo pagina de dicho articulo, 
        # y lo asignamos a la variable <pagina>
    pagina = wikipedia.page(articulo) 

        # A nuestro objeto guardado en la variable <pagina>, podemos adicionarle su metodo .summary, 
        # el cual nos retornara un string con resumen del articulo y lo asigamos a la variable <summary>  
    summary =  pagina.summary            
    #print(summary)       
        # Separamos el string <summary> en frases, valiendonos del punto "." para separarlas.
        # Esto retornara una lista con las frases y la guardaremos en la variable <frases>
    frases = summary.split(".")  

        # Solo nos interesa usar la primera frase, asi que crearemos una variable llamada <frase>
        #  y le asignaremos la primera de la lista <frases>
    frase = frases[0]             

    if " es " not in frase:   #Utilizamos el condicional if para verificar si el string " es " (con espacios) no se encuentra en la frase                
        continue              #En caso de no estar, el elemento <continue> reiniciara el bucle.

    
    #En caso de ser encontrada el String, buscamos su indice (posicion en el String) y lo guardamos en <ind>
    ind = frase.index(" es ")    
    #print(ind)
    #Cortamos el string, haciendo que este comience en el indice.
    frase = frase[ind:]   
    #print(frase)
    #Para reducir el string, separamos la frase por comas.   
    frase = frase.split(",")        
    #print(frase)
    #A nuestra variable frase le asignamos la primera frase despues de ser separada por comas.
    frase = frase[0]              
    
    #Usamos print para visualizar nuestra frase. 
    # En este ejemplo se adiciono "Python" al inicio de la frase, prueba cambiando esta palabra.       
    print(f'Poesia y Codigo{frase}')
    
    #finalmente, como obtuvimos una frase, adicionamos +1 a nuestro contador, y nuevamente se vuelve a iterar.
    contador = contador + 1        
