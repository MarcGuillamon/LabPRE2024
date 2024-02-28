class Punto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def x(self):
        """
        3.8

        :return: float
            devuelve la coordenada x
        """
        return p.__x

    def y(self):
        """
        5.6

        :return: float
            devuelve la coordenada y
        """
        return p.__y

    def modulo(self):
        """
        >>> p = Punto(3.8, 5.6)
        >>> p.modulo()
        6.767569726275452


        :return: float
            devuelve la distancia al centro
        """
        return (self.__x ** 2 + self.__y ** 2) ** 0.5

    def distancia(self, otro):
        """
        >>> p = Punto(3.8, 5.6)
        >>> q = Punto(5.8, 3.6)
        >>> p.distancia(q)
        1.343894


        :param otro: Punto
        :return:
        """
        return otro.desplazar(self).modulo()

    def desplazar(self, otro):
        return self


if __name__ == '__main__':
    p = Punto(3.8, 5.6)
    print(f"el punto esta en las coordenadas ({p.x()}, {p.y()})")
    print(f"el modulo del punto es {p.modulo()}")
    import doctest

    print(doctest.testmod())
