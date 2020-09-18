# Preparaciones!



### 1) Instalar Python 3.8.5

 *Si ya tienes python 3 instalado en tu equipo, puedes saltar este paso e instalar las [link librerias](#librerias)


Para cada sistema operativo, la instalacion de Python es diferente:

-   **WINDOWS**:

    1.   **Descargamos el archivo ejecutable para windows:**


           -    Windows-64Bits: https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe (En caso de no estar seguro, usar este)

           -    Windows-32Bits: https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe   



    2.  **Ejecutamos el archivo .exe**

    3.   **Nos aseguramos de agregar python a PATH**

    ![Image of PATH](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png)
                
    4.   **Al finalizar la instalacion, desactivamos la restriccion de longitud de los path**

    ![Deshabilitar longitud](https://i.stack.imgur.com/r6XEh.jpg)

    5. **Verificamos que python este instalado**

        Vamos al menu de Windows y tecleamos "cmd" y oprimimos ENTER para abrir la consola, y procedemos a [link verificar la instalacion.](#verificar)


-   **UBUNTU**:
            
    1. Abrimos la terminal, escribimos el siguiente codigo:

                sudo apt install python3.8

    

### 3) <a name="verificar">Verificamos la instalacion</a>

    En la terminal, escribimos:
    
                python --version

    Y debe retornarnos

                python 3.8.5

    
!       [Verificacion consola](https://i.ibb.co/JFnF49W/verificar-python-windows.png)


### 2)  <a name="librerias">Instalar librerias:</a>

Para los ejercicios y ejemplos, requerimos el uso de diferentes librerias desarrolladas por terceros para la correcta y eficiente ejecucion de los programas. Debemos instalar estas librerias:

* Abrimos la terminal y escribimos el siguiente codigo:

        pip install wikipedia spacy tweecy

Al ejecutar este comando, una serie de confirmaciones apareceran en la consola, instalando las librerias. Cuando la linea de comando vuelva a mostrar nuestra linea de usuario, habra finalizado y ya tendremos las librerias instaladas.

<sub>!!!  En caso de que exista algun tipo de error  (Texto Color Rojo) tomar pantallaso del inicio del texto rojo. Lo solucionaremos a su debido tiempo!</sub>

### 3) Instalar Visual Studio Code:

Este editor de texto tiene extensiones que nos resultaran muy útiles a la hora de programar con python, 
ademas de una consola integrada que nos permitira ver el log del output de nuestro codigo.

Para instalar, iremos a la pagina de descarga de Visual Studio Code: https://code.visualstudio.com/download
y descargaremos el instalador correspondiente a nuestro sistema operativo.

Seguimos las instrucciones del instalador y al finalizar ejecutamos el programa para cerciorarnos que funcione correctamente.




La extension de python nos permitira programar de manera mas fluida, pues crea identificadores de objetos que nos seran utiles a la hora 
de crear y leer codigo.

Para instalar, haremos click en el boton de extensiones en la barra de navegacion de la parte izquierda.



****imagen barra******

Y buscaremos la extension Python, usualmente aparece entra las populares.
En caso de no aparecer, buscarla manualmente

Hacemos click en instalar y listo.
