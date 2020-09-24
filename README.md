# Preparaciones!



### 1) Instalar Python 3.8.5

 *Si ya tienes python 3 instalado en tu equipo, puedes saltar este paso e instalar las [librerias](#librerias)


Para cada sistema operativo, la instalacion de Python es diferente:
<details>

**<summary>WINDOWS</summary>**

1. **Descargamos el archivo ejecutable para windows:**


        -    Windows-64Bits: https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe (En caso de no estar seguro si tu    sistema operativo es de 64 o 32 bits, usar este)

        -    Windows-32Bits: https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe   



2.  **Ejecutamos el archivo .exe**

3.   **Nos aseguramos de agregar python a PATH (Como se muestra en la siguiente imagen)**

![Image of PATH](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png)
            
4.   **Al finalizar la instalación desactivamos la restricción de longitud de los path**

![Deshabilitar longitud](https://i.stack.imgur.com/r6XEh.jpg)

5. **Verificamos que python este instalado**

    Vamos al menu de Windows y tecleamos "cmd" y oprimimos ENTER para abrir la consola, y procedemos a [link verificar la instalacion.](#verificar)
</details>
<details>

**<summary>MacOS</summary>**

El sistema operativo de Apple cuenta con python 2.7 por defecto, sin embargo, esta version esta desactualizada y no nos sirve para algunos ejemplos y librerias que utilizaremos.

Existen distintas maneras de instalar python en MacOS, y hemos optado por la que es, en nuestra opinion, la mas correcta. 

1) Instalar Homebrew

  Homebrew es un instalador de paquetes, el cual nos permite instalar software de repositorios publicos directamente desde la consola.

  Primero verificamos si homebrew esta instalado. Abrimos la terminal y escribimos

      brew help
  
  Si nos retorna un mensaje diciendo que el comando no existe, significa que Homebrew no esta instalado. Para instalar, escribimos esto en consola y presionamos ENTER.:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

  Nos preguntara si deseamos realizar esta instalacion, a lo que presionamos la letra <Y> para indicar Yes. Tambien nos solicitara permiso para instalar xCode, software que tambien debemos instalar:



  La instalacion demorara unos minutos, y sabremos que esta terminada cuando encontramos nuevamente nuestro nombre en la linea de comando.

  Nuevamente verificamos si brew esta instalado, escribiendo en consola:

      brew help

  Ahora deberia aparecernos algo similar a esto:



2) Instalar python 3

  Ahora podemos usar Homebrew para instalar python. En la consola, debemos escribir:

    brew install python

  La instalacion demorará unos minutos, sabremos que ha finalizado cuando en la ultima linea de la consola aparezca el nombre de nuestro mac con el usuario. 



3) Configurar Python3 como el python predeterminado

  Para configurar Python3 como el predeterminado de nuestro mac, debemos escribir dos codigos en consola:

      ln -s -f /usr/local/bin/python3.8 /usr/local/bin/python

  y

      ln -s -f /usr/local/bin/pip3.8 /usr/local/bin/pip





</details>



-   **UBUNTU**:
            
    1. Abrimos la terminal, escribimos el siguiente codigo:

                sudo apt install python3.8

    

### 2) <a name="verificar">Verificamos la instalacion</a>

   En la terminal, escribimos:
    
            python --version

   Y debe retornarnos

            python 3.8.5

    
<p align="center">
  <img src=https://i.ibb.co/JFnF49W/verificar-python-windows.png>
</p>


### 3)  <a name="librerias">Instalar librerias:</a>

Para los ejercicios y ejemplos, requerimos el uso de diferentes librerias desarrolladas por terceros para la correcta y eficiente ejecucion de los programas. Debemos instalar estas librerias:

* Abrimos la terminal y escribimos el siguiente codigo:

        pip install wikipedia spacy tweepy

Al ejecutar este comando, una serie de confirmaciones apareceran en la consola, instalando las librerias. Cuando la linea de comando vuelva a mostrar nuestra linea de usuario, habra finalizado y ya tendremos las librerias instaladas.

<sub>!!!  En caso de que exista algun tipo de error  (Texto Color Rojo) tomar pantallaso del inicio del texto rojo. Lo solucionaremos a su debido tiempo!</sub>

### 4) Instalar Visual Studio Code:

 *Si ya tienes un editor de codigo, puedes saltarte este paso.

Este editor de texto tiene extensiones que nos resultaran muy útiles a la hora de programar con python, 
ademas de una consola integrada que nos permitira ver el log del output de nuestro codigo.

Para instalar, iremos a la pagina de descarga de Visual Studio Code: https://code.visualstudio.com/download
y descargaremos el instalador correspondiente a nuestro sistema operativo.

Seguimos las instrucciones del instalador y al finalizar ejecutamos el programa para cerciorarnos que funcione correctamente.


#### Extension de Python para VS

La extension de python nos permitira programar de manera mas fluida, pues crea identificadores de objetos que nos seran utiles a la hora 
de crear y leer codigo.

Para instalar, haremos click en el boton de extensiones en la barra de navegacion de la parte izquierda.



***imagen barra***

Y buscaremos la extension Python, usualmente aparece entra las populares.
En caso de no aparecer, buscarla manualmente

Hacemos click en instalar y listo.
