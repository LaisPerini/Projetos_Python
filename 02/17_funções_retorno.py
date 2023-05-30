# Com retorno
# com mais de 1 retorno
# Desafio de aula: Cara ou Coroa

def soma2():
    numeros = []
    for n in range(2):
        numeros.append(int(input(f'Digite o {n+1} numero: ')))

    return f'somando os valores, temos: {sum(numeros)}'

print(soma2())

def par_impar():
    numero = int(input('Digite um numero: '))

    if numero % 2 == 0:
        return 'O numero é Par'
    return 'O numero é impar'

print(par_impar())

# Desafio de aula: Cara ou Coroa
from random import random, randint 
print(randint(10,20))              # retornaria numeros de 10 á 20
print(random())                    # retorna numero 1 ou 0 

def cara_cora1():
    if randint(1,2) == 1:
        return('Cara')
    else:
        return('coroa')

print(cara_cora1())

def cara_cora2():
    num = random()
    if num >=0.5:
        return('Cara')
    else:
        return('coroa')

print(cara_cora2())



