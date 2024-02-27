#Pract_excep_01
#Practica excepciones 2
# excepciones con el mensaje del sistema
if __name__ == '__main__':

    print('PractExcep_01: inicio')
    error = True
    while error:
        try:
            num = int(input('Entre Numerador: '))
            denom = int(input('Entre denominador:'))
            divisio= num/denom
            error = False
        except ValueError as err:
            print('Tipo de dato no válido : ',err)
        except ZeroDivisionError as err:
            print('División erronea : ',err)
        else:
            print('entrada correcta, dividimos')
            print('Division = %6.2f'% divisio)
        finally:
            print('Todo controlado!!')

    print('Adiós')
