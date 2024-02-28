def consulta_raw(archivo):
    # leyendo el fichero de manera completa
    f = open(archivo, 'r')
    texto = f.read()
    print(texto)
    f.close()
    print('cerrado?:', f.closed)


def consulta_lines(archivo):
    # Leer el fichero línea a línea
    f = open(archivo, 'r')
    for line in f:
        print(line[:-1])
    f.close()
    print('cerrado?:', f.closed)


def consulta_lines_with(archivo):
    # Leer el fichero colocando cada línea en una lista e imprimiendo la lista
    lineas = []
    with open(archivo) as f:
        for line in f:
            line = line.strip()
            if line != '':
                lineas.append(line)
    print(lineas)
    print('cerrado?:', f.closed)


if __name__ == '__main__':
    # leyendo el fichero de manera completa
    file = 'consulta.txt'
    consulta_raw(file)
    print('*' * 75)
    consulta_lines(file)
    print('*' * 75)
    consulta_lines_with(file)
    print('*' * 75)
