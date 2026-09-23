"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
    resultado = []  
    for n in lista:  
        if n >= 0: 
            resultado.append(n)  
    return resultado  
    


def inverte(lista):
     resultado= []
    for n in range(len(lista) -1, -1, -1):
        resultado.append(lista[n])
    return resultado
    pass


def busca_binaria(lista, alvo):
    inicio= 0
    fim= len(lista) - 1 
    while inicio<=fim:
        meio= (inicio+fim)//2
        if lista[meio] == alvo:
            return meio
        elif lista[meio]>alvo:
            fim= meio -1
        else:
             inicio= meio+1
    return -1

def intercala(lista_a, lista_b):
   resultado = []
    tam = len(lista_a)

    for i in range(tam):
        resultado.append(lista_a[i])
        resultado.append(lista_b[i])

    return resultado


def remove_repetidos(lista):
    resultado= []
    for n in lista 
     if n not in resultado
         resultado.append(n)
    return 
    pass
