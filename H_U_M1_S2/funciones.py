
inventario = []
#Se solicita el nombre del producto
def pedir_nombre():

    nombre = input("Ingrese el nombre del producto: ")
    while not nombre.replace(" ","").isalpha():
        print("Error ingrese solo letras")
        nombre= input("Ingrese el nombre del producto: ")
    return nombre
    
#Se solicita el precio del producto
def pedir_precio ():
    valido = False
    while valido == False:
        try:
            precio = float(input("Ingrese el precio del producto:"))
            if precio > 0:
                valido = True
            else:
                print("El precio debe ser mayor a 0")
        except:
            print("Error ingrese numeros sin puntos ni comas")
    return precio

#Solicitamos la cantidad del producto 
def pedir_cantidad ():  
    valido = False                  
    while valido == False :
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad > 0:
                valido = True
            else:
                print("La cantidad debe ser mayor a 0")
        except:
            print("Error ingrese una cantidad sin comas,ni puntos")   
    return cantidad
          
#En esta funcion reutilizamos las demas funciones para generar un bucle y guardar los datos recopilados en las entradas anteriores
def agregar_producto() :
    agg = "si"

    while agg == "si":
        nombre = pedir_nombre()
        precio = pedir_precio()
        cantidad = pedir_cantidad()  

        producto = {
            "nombre" : nombre,

            "precio" : precio,

            "cantidad": cantidad
        }
        inventario.append(producto)

        agg = input("¿Desea agregar otro producto? (si/no): ").lower()
         
#En esta funcion mostramos que hay en la lista llamada (inventario)
def mostrar_inventario ():
    if len(inventario) == 0:
        print("No hay nada en el inventario")
    else:
        for i in inventario:
            print(f"Nombre:{i['nombre']} Precio:{i['precio']} Cantidad:{i['cantidad']}")
#En esta funcion calulamos las estadisticas tales como el total del inventario y el total de los productos registrados
def calcular_estadisticas():
    for p in inventario:
        total = sum(p["precio"]*p["cantidad"]for p in inventario)  
        total_productos = sum(p["cantidad"]for p in inventario)
    print("El total del inventario es:",total)
    print("El total de productos registrados es:",total_productos)  
    return total,total_productos

