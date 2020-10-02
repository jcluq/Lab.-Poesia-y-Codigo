# # # # #        __  ___                        __            
# # # # #       /  |/  /___ _____  __  ______ _/ /            
# # # # #      / /|_/ / __ `/ __ \/ / / / __ `/ /             
# # # # #     / /  / / /_/ / / / / /_/ / /_/ / /              
# # # # #    /_/  /_/\__,_/_/ /_/\__,_/\__,_/_/
# # # # #        __        _____               
# # # # #   ____/ /__     / ____/___ _____ ___  ____  ____ 
# # # # #  / __  / _ \   / /   / __ `/ __ `__ \/ __ \/ __ \
# # # # # / /_/ /  __/  / /___/ /_/ / / / / / / /_/ / /_/ /
# # # # # \__,_/\___/   \____/\__,_/_/ /_/ /_/ .___/\____/ 
# # # # #       ____        __  __          /_/
# # # # #      / __ \__  __/ /_/ /_  ____  ___            
# # # # #     / /_/ / / / / __/ __ \/ __ \/ __ \             
# # # # #    / ____/ /_/ / /_/ / / / /_/ / / / /             
# # # # #   /_/    \__, /\__/_/ /_/\____/_/ /_/              
# # # # #       _____/ /                           
# # # # #      '------'
# # # # #       python







####################-Manual de Campo de Python-#######################
########
##Esta guia fue creada por Lasintetica para el laboratorio de Poesia y Codigo


###En python, comentamos usando un numeral o hash antes del texto que deseamos comentar
###Todo lo comentado de esta manera no correra en el programa. 


"""
Si usamos tres comillas " o  apostrofes '
podemos comentar multiples lineas.
Todo lo comentado de esta manera en este tutorial
es codigo que se puede ejecutar
"""

### Cuando usamos lengajes de programacion, 
### es importante tener metodos de entrada y salida que nos permitan comunicarnos con el usuario
### En python, esto se hace con el metodo print()"""

### Este tutorial tiene la intencion de demostrar el funcionamiento
### cuando veas que existe codigo escrito entre tres commillas """
### elimina estas para poder visualizar el codigo

"""
print("hola mundo, como estas mundo, mucho gusto mundo")
"""

### Los lenguajes de programacion se valen de VARIABLES para almacenar datos
### por ejemplo, aqui utilizaremos la variable <texto> y almacenaremos un saludo alli,
### el cual posteriormente utilizaremos en la funcion print() para ver el resultado en consola
### para asignar una variable escribimos: variable = dato


"""
texto = "este es un saludo!"
print(texto)
"""

### Existen diferentes tipos de datos, los cuales llamamos PRIMITIVOS, estos son:

####    char = 'a' (caracter)
####    int = 4 (numero entero)
####    float = 3.14 (numero real)
####    Boolean = True (Booleano)
####    String = "esto es un string"

### Python es un lenguaje dinamico, el cual no requiere declarar el tipo de variable, 
### pues el reconoce y asigna el tipo de manera automatica

### Veamos los diferentes tipos de variables y sus metodos mas comunes


########### Numeros (int y float) ################

### Con los numeros enteros podemos hacer operaciones matematicas con +,-,/,*

"""
x = 5
y = 9
z = 0.5

print(x+y) #suma
print(y-x) #resta
print(y/x) #division
print(y*z) #multiplicacion
"""

############ Booleanos #############

### Los booleanos son datos que equivalen a verdadero o falso, y tambien pueden ser representados como 1 y 0.
### 
"""
a = True
b = False

print(a is True) #Es <a> True ? -> True
print(a is False) #es <a> False 4 ? -> False
print(a is b) #es <a> igual a <b> ? -> False
"""

### Existen tambien operadores logicos, cuyos resultados nos daran un booleano

"""
numero = 10
print(numero > 5) # Es <numero> mayor que 5? -> True
print(numero <= 5) # Es <numero> igual o menor que 5? -> False
print(numero == 10) # Es <numero> igual a 10? -> True

respuesta = (numero is 10) #tambien podemos guardar el resultado de las operaciones en variables!
print(respuesta)
"""

################ STRINGS ###################################################

### La palabra string traduce cuerda, en este caso significa cuerda de caracteres.

### Podemos sumar los strings

"""
a = "este es un string"
b = " este es otro string"
print(a+b)
"""

### Otra forma de sumar variables en strings!

"""
a= "yo tambien soy un String"
b= "yo igual"
print(f"Yo soy un String, {a} y {b}")
"""

### Los strings funcionan similar a las listas! (¿Que es una lista?)

"""
a = "Esto es un String" #Nuestro String original
b = a[0] #aqui asignamos a la variable <b> el primer caracter de a, es decir "E"
c = a[5:10] # tambien podemos establecer substrings , en este caso, se imprimiran los caracteres entre 5 y 10

print(a)
print(b)
print(c)
"""

### Metodos utiles e importantes para Strings!!! (Que es un metodo???)

"""
a = "YO soy el ejemplo, osea un String"

print(len(a)) # len(String) nos sirve para conocer la longitud de un String
print(a.upper()) # .upper() retorna el string en mayusculas
print(a.lower())   #.lower() retorna el string en minusculas
print(a.capitalize()) #.capitalize() retorna el primer caracter en mayuscula y el resto en minusculas. 
print(a.index("el")) #index(subString) Retorna la primera posicion encontrada del subString 
"""


### split(String)
### split() separa un String. Utiliza un string para definir las posiciones de corrte
### y retorna una lista con estas frases.


"""
a = "Soy una frase. Yo tambien soy una frase." # nuestra frase
b = a.split(".")
print(b)

"""

##### Listas ################################################################################# 

### Las listas son objetos de python que nos sirven para guardar multiples objetos dentro de ellas.

"""
a = 3  
b = "String"
lista = [a,b,8,"palabra",True] #En las listas podemos guardar diferentes tipos de datos y variables, en diferentes combinaciones.
print(lista) #podemos imprimir toda la lista

print(lista[0]) #tambien podemos seleccionar un solo elemento de la lista
print(lista[2:]) #podemos cortar los elementos de la lista, en este caso [2:] significa "Todos los elementos de la lista despues de la posicion 2"
print(lista[1:4]) #tambien podemos definir , en este caso [1:4] significa "Todos los elementos de la lista contenidos entre la posicion 1 y 4"
"""

########## Metodos Listas ########################################################################
"""
lista = ["a","b"]
letra = "c"
print(lista)

lista.append(letra) ### Con .append(<dato>) adicionamos un dato al final de nuestra lista.
print(lista)

lista.insert(0,"1") ### podemos usar .insert(<posicion>,<dato>) para insertar un dato en una posicion de la lista
                    ### los datos se desplazar hacia el final para dar lugar al nuevo dato.
print(lista)

lista.pop()         ### Con .pop() eliminamos el ultimo elemento de la lista.
print(lista)

del(lista[1])        ### .del(<lista>[posicion]) nos sirve para eliminar el elemento en determinada posicion.
print(lista)

"""

##########################
###Podemos sumar listas!
"""
lista_a = ["Una","lista"]
lista_b = ["otra","lista"]

lista_suma = lista_a + lista_b
print(lista_suma)
"""

##############################
### podemos juntar el contenido de una lista en un solo digito, para esto usamos <separador>.join()

"""
lista = ["Esto","es","un","ejemplo"]
frase = " ".join(lista)
print(frase)

frase = "".join(lista)
print(frase)
"""
###############################
## len() y in ? 
"""
lista = [1,2,6,345,2,7,788654,"foo","bar"]
longitud = len(lista) ###podemos usar len(<lista>) para conocer la longitud de una lista
print(longitud) 

respuesta = 2 in lista ###  <dato> in <lista> nos retorna un booleano respondiendo si un dato se encuentra en una lista.
print(respuesta)

if 2 in lista:
    print("si esta en la lista!")
"""

#######   CONDICIONALESS   #####################################################################

#### para formular un condicional, nos valemos de la palabra <if>

"""
a = 3
if a > 2 : #la sintaxis: if <operacion con retorno booleano> :    ***Es imperativo escribir <:> al final del condicional. 
    
    print("El condicional se cumple!") #Se define el codigo a ejecutar cuando el condicional se cumple. 
    print("yay")                       #El codigo a ejecutarse debe estar separado del margen por una tabulacion de distancia!

print("Yo estoy afuera del condicional")
"""

### podemos insertar condicionales dentro de condicionales!


"""
a = 5

if a >2:
    print("a es mayor que 2")   
    if a is 5:                 #todo el codigo, incluyendo el segundo condicional se indentan en la misma linea
        print("a es igual a 5!")

    print("esto se imprimira si a > 2")
"""

############################
### if, elif, else
"""
x = 7

if x > 8:                       #condicion inicial
    print("x es mayor que 8")
elif x < 6:                     #si la primera condicion no se cumple podemos evaluar otra con <elif> (else if)
    print("x es menor que 6")
else:                           #si ninguna condicion se cumple, podemos utilizar <else> para ejecutar codigo
    print("x es menor que 8  y mayor que 6")
"""

##############################################
####### and y or ##############
"""
a = 5
b = 7

if a > 4 and b > 5: ### podemos usar <and> en un condicional para agregar condicionales.
    print("ambas condiciones se cumplen!")

if a == 7 or b == 7: ### podemos usar <or> cuando deseamos que el codigo se ejecute si almenos un condicional se cumple
    print("una de las condiciones se cumple!")
"""
###################################################################################

#########_______ITERADORES___________########################

###### while ##############

### Utilizamos el iterador <while> para correr un codigo de forma repetitiva (un loop), hasta que la condicion dada deje de ser cierta.

"""
contador = 0                    #nuestro contador inicia en 0

while contador < 8:             #el iterador funcionara en loop mientras el contador sea menor que 8
    print(contador)             #imprimos el valor del contador
    contador = contador + 1     #sumamos 1 a nuestro contador en cada iteracion.
"""


##### for #######################

### Podemos utilizar el iterador <for> para repetir un proceso una cantidad de veces definida:

"""
for x in range(20): #La formula que utilizamos es for <variable> in range(<cantidad de iteraciones>)
    print(x)
    print("holaaaa")
"""
### tambien podemos utilizar <for> para iterar listas!

"""
frase = "Esto es una frase"
lista = frase.split(" ")
print(lista)
for elemento in lista:  #La formula que utilizamos es for <variable> in range(<cantidad de iteraciones>)
    print(elemento)

"""


### PEND 
### METODOS
### CLASES
### SEPARAR ESTA GUIA EN DIFERENTES ARCHIVOS!!!!!!!!
