####################Tutorial de Python#######################

###En python, comentamos usando un numeral o hash antes del texto que deseamos comentar
###Todo lo comentado de esta manera en este programa es texto


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

################ STRINGS ###########

### La palabra string traduce cuerda, en este caso significa cuerda de caracteres.

### Podemos sumar los strings

a = "este es un string"
b = " este es otro string"
print(a+b)