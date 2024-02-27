#Pract_excep_01
#Practica excepciones 1
#No hay control de excepciones
# se acba con un ctrl+C
def main():
    print('PractExcep_01: inicio')
    while True:
        num = int(input('Entre Numerador: '))
        denom = int(input('Entre denominador:'))
        divisio= num/denom
        print('%0.4f'% divisio)
    print('Adiós')

if __name__ == '__main__':
    main()
