# -*- coding: utf-8 -*-
def leer_fichero_csv(fichero):
    import csv

    lista = []
    with open(fichero, "r") as fichero_csv:
        datos = csv.reader(fichero_csv, delimiter=";", quotechar="'")
        for fila in datos:
            f = fila[:3] # los 4 primeros datos son string y no requieren conversion
            for v in fila[3:]:
                f.append(float(v))# el resto lo pasamos a float y lo añadimos a la lista f
            lista.append(f)
    return lista

def saldo_final(id, lista):
    for persona in lista:
        if persona[0] == id:
            saldo = sum(persona[5:])
            return round(saldo, 2)


def evolucion_saldo(id, lista):
    evolucion = []
    for persona in lista:
        if persona[0] == id:
            saldo = persona[5]
            evolucion = [saldo]
            for mov in persona[6:]:
                saldo += mov
                evolucion.append(round(saldo, 2))
    return evolucion


def numeros_rojos(id, lista):
    numeros = evolucion_saldo(id, lista)
    for numero in numeros:
        if numero <= 0:
            return True
    return False


def ingresos_y_gastos(id, lista):
    ing = []
    gas = []
    ing_gas = [[], []]
    for persona in lista:
        if persona[0] == id:
            movimientos = persona[6:]
            for mov in movimientos:
                if mov >= 0:
                    ing.append(mov)
                else:
                    gas.append(mov)
        ing_gas[0] = round(sum(ing),2)
        ing_gas[1] = round(sum(gas),2)
    return ing_gas


def MaxMov(lista):
    maxmov = 0
    maxnom = ''
    for persona in lista:
        nummov = len(persona[6:])
        if nummov > maxmov:
            maxmov = nummov
            maxnom = persona[1]
    return maxnom, maxmov

def doc():
    """
    >>> lista = [['36987701H', 'Joan M Arnan Comellas', "L'Hospitalet De Llobregat",\
    '67', 304.38, 12.4, -57.47, 216.81, -41.61, 102.34, 23.38, 155.97, -402.64, -230.69],\
    ['45544180W', 'Elisenda Blanco Requejo', 'Mataró³', '55', 234.95, -131.36, -56.07,\
    -15.51, 47.64, -55.61, -88.49], ['46743545X', 'Maria Cristina Caleya Fermoselle',\
    'Vic', '52', 717.38, -75.95, -35.87, -78.28, 156.56, 51.78, -448.85, -126.37, -225.98,\
    -266.58, -13.53], ['52274788C', 'Esther Collado Salgado', 'Vic', '45', 278.57, 164.52,\
    46.07, -324.84, -11.66, -2.22, -465.06, -120.8, -265.6], ['47614167Y',\
    'Regina Charles Piedra', 'Cerdanyola Del Vallés', '52', 385.68, 323.49, -326.09,\
    97.31, -12.43, -191.78, 46.96, -291.81], ['46755157O', 'Angel Fabrego Escamilla',\
    'Lleida', '41', 545.58, -212.1, 119.86, -227.02, -46.48, 503.4, 129.17, 76.07]]
    >>> id = '47614167Y'
    >>> saldo_final(id, lista)
    -354.35
    >>> id = '46755157O'
    >>> evolucion_saldo(id, lista)
    [-212.1, -92.24, -319.26, -365.74, 137.66, 266.83, 342.9]
    >>> id ='46743545X'
    >>> numeros_rojos(id, lista)
    True
    >>> id = '36987701H'
    >>> ingresos_y_gastos(id, lista)
    [498.5, -732.41]
     >>> MaxMov(lista)
     ('Maria Cristina Caleya Fermoselle', 9)
    """
    pass
if __name__ == '__main__':
    import doctest
    
    print(doctest.testmod())
    import csv

    lista = leer_fichero_csv('ListaFinanciera.csv')
    print('Listar los tres con más saldo_final')
    lista.sort(reverse=True, key = lambda x : sum(x[4:]))
    for elemento in lista[:3]:
        print('Nombre: %s, saldo: %0.2f€'%(elemento[1],sum(elemento[4:])))
    input('pulsa intro para seguir...')
    for persona in lista[:3]:
        print('Datos del usuario %s:' % persona[1])
        id = persona[0]
        print('Saldo actual               : %0.2f' % saldo_final(id, lista))
        print('Evolucion del saldo        : %s' % evolucion_saldo(id, lista))
        print('Ha estado en numeros rojos?: %s' % numeros_rojos(id, lista))
        print('Lista de Ingresos y Gastos : %s' % ingresos_y_gastos(id, lista))
        print('\n')
    print('\nUsuario con más movimientos del período : %s con %d movimientos' % MaxMov(lista))
