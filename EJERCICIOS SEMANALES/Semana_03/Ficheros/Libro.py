# -*- coding: utf-8 -*-
def libro_visitas(archivo):
    with open(archivo,'a') as fichero:
        nombre = input('introduce tu nombre: ')
        while nombre != '':
            print('bienvenido,',nombre)
            fichero.write(nombre+'\n') #escribir el nombre y el caracter de final de línea
            nombre = input('introduce tu nombre: ')

if __name__ == '__main__':
    from consulta import consulta_lines as listado
    file = 'libro_firmas.txt'
    libro_visitas(file)
    listado(file)

