from Ingresar.Ingresar import z
from Modificar.Modificar import *

def eli(lis):
   eliminar = str(input('Producto a eliminar: '))
   for x in range(len(lis)):
    if eliminar in lis[x]:
        lis.remove(eliminar)
        print("Eliminación exitosa", lis)
        exit()
    else:
       print("Su producto no está disponible", eliminar)
       exit()
eli(z)