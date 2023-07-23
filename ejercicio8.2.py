"""
     Escribir una función que reciba una lista de números no ordenada, que:
        a) Devuelva el valor máximo.
        b) Devuelva una tupla que incluya el valor máximo y su posición.
        c) ¿Qué sucede si los elementos son cadenas de caracteres?
        
        Nota: no utilizar lista.sort()

"""

def buscar_max_valor(lista):

    valor_maximo = 0

    for num in lista:
        if num > valor_maximo:
            valor_maximo = num


    return valor_maximo

# print(buscar_max_valor([10,1,3,50,6,29,19,30,22]))



def buscar_max_valor_2(lista):

    valor_maximo = 0

    for i in range(0,len(lista)):
        if lista[i] > valor_maximo:
            valor_maximo = lista[i]
            posicion = i + 1

    return tuple((valor_maximo, posicion))

# print(buscar_max_valor_2([10,1,3,50,6,29,19,30,22]))



def buscar_max_valor_3(lista):

    valor_maximo = 'a'

    for i in range(0,len(lista)):
        if lista[i] > valor_maximo:
            valor_maximo = lista[i]
            posicion = i + 1

    return tuple((valor_maximo, posicion))

print(buscar_max_valor_3(['sol', 'as', 're', 'wa', 'dr', 'ex', 'oc', 'zq']))












