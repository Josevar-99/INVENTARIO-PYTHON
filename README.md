# GUIA INSTALACION PROGRAMA INVENTARIO
-------
Este programa funciona para la ingreso de productos a un inventario,puedes agregarle nombre, precio y las cantidades de productos que con las que cuentes en tu inventario

---
## ESTRUCTURA DEL REPOSITORIO
- README.MD
- Inventario.py
- imagenes

---

## DESCARGA DEL PROGRAMA

Para poder hacer uso del programa, se deben realizar una serie de pasos basicos para poder ejecutar el archivo a continuacion veremos los pasos necesarios para ejecutarlo

1. Abre la terminal :  en tu dispositivo si es linux, presiona las teclas, **control**,**alt**, y la tecla de la letra **T** al mismo tiempo se abrira la ventana terminal aparecera algo asi:

![alt text](<Captura desde 2026-03-13 17-43-58.png>)

Si es en windows presiona la tecla **windows** + la tecla de la letra **R** te aparecera algo asi:
![alt text](<Captura desde 2026-03-13 17-46-53.png>)

dentro del cuadro abrir escribimos **CMD**
nos abrira la ventana de **CMD** algo asi:
![alt text](<Captura desde 2026-03-13 17-49-56.png>)

2.Copiamos el repositorio: desde la consola escribimos este comando en el caso de linux ejecutamos el siguiente comando:
```bash
 CD /Escritorio 
 git clone https://github.com/Josevar-99/INVENTARIO.git
```
 en windows ejecutamos
```bash
  CD / Desktop
```
presionamos enter     y luego copiamos y pegamos el comando:
 ```bash
  git clone https://github.com/Josevar-99/INVENTARIO.git
```
3. Este archivo utiliza el lenguaje python si no sabemos si lo tenemos intstalado instala python con este comando
```bash
sudo apt update
sudo apt install python3 python3-pip
```
en windows
Descarga: Ve a la página oficial de Python y descarga la última versión para Windows.
Instalación: Abre el instalador descargado.
Configuración Importante:

¡Fundamental! Marca la casilla "Add Python to PATH" en la parte inferior de la primera pantalla.
    Selecciona "Install Now" (Instalar ahora).
    Si se solicita permiso de administrador, haz clic en "Sí".

Finalizar: Haz clic en "Close" al terminar la instalación.
Verificación: Abre el "Símbolo del sistema" (busca cmd en el menú de inicio) y escribe:
python --version
Debería aparecer la versión de Python instalada (ej. Python 3.12.x)

4.despues que instalamos python,ejecutamos  desde la consola de comandos:
```bash
CD/Escritorio
CD/INVENTARIO
phyton3 Inventario.py
```
en linux 
en Windows ejecuta el siguiente comando:
```bash
CD/Desktop
CD/INVENTARIO
python Inventario.py
```
---
## PUESTA EN MARCHA DEL PROGRAMA

Despues de ejecucion del programa deberias ver algo asi:
ingresa el nombre que deseas para el producto
![alt text](<Captura desde 2026-03-13 18-43-05.png>)
ingresa el precio que deseas para el producto
![alt text](image.png)
ingresa la cantidad de productos que tienes
![alt text](<Captura desde 2026-03-13 18-46-08.png>)
Luego de teminar el ingreso de los datos, el programa mostrara un resultado asi:
![alt text](<Captura desde 2026-03-13 18-51-09.png>)

---
## RECOMENDACIONES 

En la entrada de datos nombre (abajo la imagen) puedes poner cualquier nombre que deseas
![alt text](<Captura desde 2026-03-13 18-43-05.png>)

En la entrada precio solo debes ingresar numeros mayores a 0 si colocas un numero negativo te lo pedira otra vez hasta que ingrese un numero valido:
![alt text](image-1.png)

En la entrada cantidad de datos solo puedes ingresar numeros enteros, sin decimales ni comas, ni numeros negativos si lo hace saldra algo asi:
![alt text](image-2.png)

---
## DIAGRAMA DEL PROGRAMA 

![Diagrama del proyecto](imagenes/Diagrama%20inventario_page-0001.jpg)

