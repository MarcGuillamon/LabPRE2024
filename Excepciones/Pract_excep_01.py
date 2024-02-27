# Pract_excep_01
# Practica excepciones 1
# hay control de excepciones
# se acba con un ctrl+C
def main():
    print('PractExcep_01: inicio')
    while True:
        try:
            num = int(input('Entre Numerador: '))
            denom = int(input('Entre denominador:'))
            divisio = num / denom
        except ValueError as err:
            print('Valor no válido', err)
            divisio = 0
        except ZeroDivisionError:
            print('division por cero')
            divisio = 0
        finally:
            print('Division = %6.2f' % divisio)


if __name__ == '__main__':
    main()
