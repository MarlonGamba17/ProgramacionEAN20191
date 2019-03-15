def Numero_Flotante(num):
    '''
    float -> str

    >>> Numero_Flotante(10)
    "El numero es positivo"

    >>> Numero_Flotante(-10)
    "El numero es negativo"


    :param num: Numero_Flotante
    :return: str que nos dice si el num es < 0
    '''

    if num < 0:
        return 'El numero es negativo'
    elif num >= 0:
        return 'El numero es positivo'

print('valide el numero -15: '+ Numero_Flotante(-15))



