"""
While com Break

while True: >>> este laço será executado enquanto não encontrar o Break pelo caminho.

Break >>> Condição de parada de um loop.
"""


# Validando tipo de dado com break
while True :
    sair = str(input('Tecle S para sair: ')).upper()
    if sair == 'S':
        break                                     #break serve para encerrar o loop


while True:
    nome = input('Nome: ')

    if not nome.isnumeric():                    # isnumeric verifica se realmente um numero
        print(f'{nome}, bem vindo')
        break
        
    else:
        print('Por favor, digite seu Nome: ')
                               
print('o programa continuou')