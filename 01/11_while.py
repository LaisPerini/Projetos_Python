"""
While >>> Utilizada quando se sabe a quantidade de repetições e
quando não se sabe.
* Necessário atentar para o critério de parada.

Sintaxe >>>  while expressão_bool:
                    Execução.

Expressão será executada enquanto for verdadeira.
Expressão Booleana >>> Toda expressão onde o resultado
for Verdadeiro ou Falso.

Ex.
resposta = ''
    while resposta != 'SIM':
            resposta = 'input'
"""

# repetindo um texto 5 vezes com for

for txt in range(5):
    print('Suco de Fruta:')

# repetindo um texto 5 vezes com while
inicio = 0
while inicio<5:
    print('Suco de Fruta:')
    inicio += 1

# validando uma senha de forma simples
# sair do loop é clt+c

senha_cadastrada = '102030'
senha_digitada = ''

while senha_digitada != senha_cadastrada:
    senha_digitada = str(input('digite sua senha: '))
