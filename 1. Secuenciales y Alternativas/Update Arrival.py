"""
Write a function update_arrival(h, m, d) that given integers 0 ≤ h < 24 and 0 ≤ m < 60 representing a flight time
arrival and d ≥ 0 representing a delay in minutes returns the updated time arrival.

Escriba una función update_arrival(h, m, d) que, dados los números enteros 0 ≤ h < 24 y 0 ≤ m < 60 que representan la
hora de llegada del vuelo y d ≥ 0 que representa un retraso en minutos, devuelva la hora de llegada actualizada.
"""


def update_arrival(h, m, d):
    """
    >>> update_arrival(10, 45, 20)
    (11, 5)
    >>> update_arrival(12, 30, 60)
    (13, 30)
    >>> update_arrival(22, 0, 120)
    (0, 0)
    >>> update_arrival(23, 57, 5 + 24*60)
    (0, 2)
    """

    return (h + ((m + d) // 60)) % 24, (m + d) % 60


if __name__ == '__main__':
    import doctest

    print(doctest.testmod(verbose=True))
