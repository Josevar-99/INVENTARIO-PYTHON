
#Solicita el nombre del producto al usuario
nombre = input("Ingrese el nombre del producto:")

#Solicita el precio de producto al usuario "verifica que el precio digitado sea positivo"

while True:
    try:
        precio = float(input("Ingrese el precio del producto:"))
        if precio > 0:
            break
        else:
            print("el precio debe ser mayor a 0")
    except ValueError:
        print("ingrese numeros mayor a 0")        

#Solicita a usuario la cantidad del producto "verifica que la cantidad digitada sea positiva"
while True:
    cantidad = input("Ingrese la cantidad del producto: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error: ingrese un número entero positivo")

#Variable que contiene la operacion matematica para el resultado final 
costo_total = (precio * cantidad)

#General el resultado visualmente,con las cantidades anteriormente ingresadas con el costo total
print("\nproducto:",nombre,"\nprecio:",precio,"\ncantidad:",cantidad,"\ntotal:",costo_total)


# este programa solicita a usuario un nombre para un producto,solicita el precio que tiene o debe
#tener el producto  y ademas solicita a el usuario la cantidad que tiene el usuario en existencia,
#despues de obtener estos dos valores el programa realiza un operacion aritmetica, multiplica el 
#precio del producto ingresado, por la cantidad de productos ingresados, mostrando asi en el bash
#el nombre del producto, mas el precio, la cantidad y el costo total de los productos ingresados.