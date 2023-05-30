"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> inicio, fim, passo
* Enumerate -> Permite acesso ao índice
"""


for item in range(10,101,10):                        #range sempre vai ter (começa,termina,conta o passo)
    print(item)                                        

for item in range(2):
    nome = str(input('Nome: '))
    print(nome)



# Crie um sistema que receba 4 notas e calcule a média

soma=0
for n in range(0,5):
    print(f'Variavel Soma: {soma}')
    nota = float(input(f'\nDigite a nota: {n+1}ª nota: '))
    soma += nota                                               # soma = soma + nota daria o mesmo resultado    
media = soma/n
print(media)

