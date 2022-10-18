import Ingresar.Ingresar
def mod(list):
    cambio = input('Producto a cambiar: ')
    if cambio in list:
        for x in range(len(list)):
            if cambio == list[x]:
                list[x] = input('Nuevo valor: ')
                print('El nuevo valor es: ', list[x])
                print('La nueva lista es: ', list) 
                list.sort()
                print('La lista ordenada es: ', list)
                return list
              