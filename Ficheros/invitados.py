# -*- coding: utf-8 -*-
def invitados(archivo,modo):
    nombre = input('introduce tu nombre: ')
    print('bienvenido,',nombre)
    with open(archivo, modo) as fichero:
        fichero.write(nombre+'\n') #escribir el nombre y el caracter de final de línea




if __name__ == '__main__':
    # Crea un archivo nuevo con un nombre
    file = 'invitados.txt'
    invitados(file,'w')
    invitados(file,'x')
    invitados(file,'a')

