#Pract_excep_01
#Practica excepciones 1
#control de excepciones generico

import sys
print('PractExcep_01: inicio')
d = True
while d:
    try:
        num = int(input('Entre Numerador: '))
        denom = int(input('Entre denominador:'))
        divisio= num/denom
        print('Division = %6.2f'% divisio)
        d = False
    except: # excepcion generica
        print("Error:", sys.exc_info()[1])

