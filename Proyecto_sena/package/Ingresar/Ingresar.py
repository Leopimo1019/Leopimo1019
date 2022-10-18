from Modificar.Modificar import mod
def ing():
    cantidad = int(input("Ingrese la cantidad de productos a ingresar: "))
    global productos 
    productos = []
    print("La cantidad de productos ingresada es: ", cantidad)
    for x in range(cantidad):
        po = input("Ingrese el producto: ")
        productos.append(po)
        x+=1
        print("Prodcuto número: ", x)
    for k in productos:
       print("Los productos son: ", k)
    return productos
z = mod(ing())