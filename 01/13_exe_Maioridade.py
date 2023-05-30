"""
 Faça um programa que leia ano de nascimento de 5 pessoas e no final
 mostre quantas pessoas já atingiram a maioridade e para aquelas que
 ainda atingiram, mostre a média em anos que faltam para chegarem a maior idade.
"""

from datetime import datetime

ano_atual = datetime.today().year
maior_idade = menor_idade = soma = 0

for a in range(2):
    ano_nasc = int(input('Digite seu Ano de Nascimento: ')) 
    idade = ano_atual - ano_nasc

    if idade>=18:
        maior_idade +=1
    else:
        menor_idade +=1
        soma = 18 - idade
        

media = soma/menor_idade 
print(maior_idade)     
     


    
