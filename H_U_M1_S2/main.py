#Se importan las funciones desde el archivo funciones
import funciones


#Declaramos el inventario en una lista y la variable opcion
inventario = []
opcion = ""


#Encapsulamos en un bucle while el menu, para que se ejecute cada vez que salgamos,
# de las opciones elegidas 

while opcion != "4":

        print("================================")
        print("====BIENVENIDO AL INVENTARIO====") #mensaje de bienvenida
        print("================================")


#Mostramos el menu al usuario en la consola 
        print("Menu")
        print("1.Agregar un producto")
        print("2.Mostrar inventario")
        print("3.Valor total del inventario,Cantidad total de productos registrados.")
        print("4.Salir.")
        
#Solicitamos al usuario ingresar una opcion
        opcion = input("Ingrese una opcion: ") 
#Encapsulamos en validaciones por cada entrada de usuario,si el usuario ingresa un opcion invalida solicitara al usuario una opcion hasta que sea valida
        if opcion == "1":
            funciones.agregar_producto() #llamamos a las funciones desde cada opcion digitada por el usuario 
               
        elif opcion == "2":
            funciones.mostrar_inventario() 
                                
        elif opcion == "3":
            funciones.calcular_estadisticas()
             
        elif opcion == "4":
            print("Gracias por utilizar el inventario,Hasta luego")#Generamos un mensaje de despedida para el usuario
        else:
             print("Ingrese una opcion valida")

#En resumen el objetivo de esta semana es cononcer los diferentes estructuras de colecciones,tales como tuplas,diccionarios
#y listas tambien resaltamos el uso de las funciones y sus multiples usos dandonos  en la escritura de codigo limpia
#resumiendo operaciones y estructuras de codigo.

    




      

    



