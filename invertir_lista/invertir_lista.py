def invertir_lista(lista):
    '''
    >>> invertir_lista(['a', 10, 'marlon', True])
    [True, 'jose', 10, 'a']
    
    :param lista: 
    :return: 
    '''

    resultado = []
    # for i in range(-1,-len(lista) -1, -1):
    #    resultado.append(lista(i))
    # for elemento in lista:
    #    resultado.insert(0, elemento)
    copia = lista.copy()

    while copia:
        resultado.append(copia.pop())

    return resultado


def preguntas_usuario(dato):
    '''
    >>> preguntas_usuario('4')
    sebastian es loca 2

    :param datos:
    :return:
    '''
    dato = 2
    while dato /2 == 0:
        dato = int(input('ingrese un dato'))

        print(dato)

    print('sebastian es loca' , dato)




print(preguntas_usuario('a'))
