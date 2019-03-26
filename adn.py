def obtener_complemento(base):
    """
    (str) -> str

    La función obtener complento que retorna el complemento de una base

    >>> obtener_complemento('A')
    'T'
    >>> obtener_complemento('T')
    'A'
    >>> obtener_complemento('C')
    'G'
    >>> obtener_complemento('G')
    'C'

    :param base:
    :return: str complemento obtenido
    """
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'C':
        return 'G'
    else:
        return 'C'


    # retorna caracter

def generar_cadena_complementaria(adn):
    """
    (str) -> str

    La función para generar la cadena complementaria

    >>> generar_cadena_complementaria("GATA")
    'CTAT'

    :param adn:
    :return: str la cadena complementaria
    """

    cadena_complemento = ""

    for base in adn:
        cadena_complemento = cadena_complemento + obtener_complemento(base)

    return cadena_complemento


def calcular_correspondencia(adn1, adn2):
    """
    (str, str) -> float

    La función para calcular el porcentaje de correspondencia de una cadena y otra


    :param adn1:
    :param adn2:
    :return:
    """
    longitud_adn1 = len(adn1)
    longitud_adn2 = len(adn2)
    porcentaje = 0.0

    if longitud_adn1 > longitud_adn2:
        if (adn2 in adn1):
            porcentaje = longitud_adn2 / longitud_adn1
    else:
        if (adn1 in adn2):
            porcentaje = longitud_adn1 / longitud_adn2

    return porcentaje
    # retorna num


def corresponden(adn1, adn2):
    """
    (str) -> bool

    La función que nos valida la correspondencia entre dos cadenas

    >>> corresponden(GATA)
    true

    >>> corresponden(GATAR)
    false

    :param adn1:
    :param adn2:
    :return:
    """
    if (adn1) == 

    # retorna Bool
    pass


def es_cadena_valida(adn):
    pass


def es_base(caracter):
    pass


def es_subcadena(adn1, adn2):
    pass


def reparar_dano(adn, base):
    pass


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

