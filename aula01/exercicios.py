"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    soma=0
    for n in lista:
     soma= soma+n 
     print(soma)
    


def conta_pares(lista):
    cont=0
    for n in lista:
        if n % 2 == 0:
          cont= cont + 1
    print(cont)


def maior_valor(lista):
    maior=lista[0]
    for n in lista:
      if n>maior:
       maior = n
    print(maior)

def existe(lista, alvo):
    for n in lista:
        if n == alvo:
            print("true")
            break
    else:
        print("false")


def busca_linear(lista, alvo):
    posicao=0
    for n in lista:
        if n == alvo:
            posicao= lista.index(alvo)
            print(posicao)
        else:
            print(-1)


def segundo_maior(lista):
    maior = float('-inf')
    segundo_maior = float('-inf')

    for n in lista:
     if n > maior:
         segundo_maior = maior 
         maior = n              
     elif n > segundo_maior and n != maior:
         segundo_maior = n     

    print(segundo_maior)
