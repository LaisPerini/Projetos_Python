"""
Cadastre 3 produtos no estoque, cada produto precisa ter:
- nome
- preço
- data e hora que foi cadastrado
- Nome do Funcionário

Em seguida, permita que os produtos sejam visualizados.
"""

from datetime import datetime


estoque=[]


for i in range(2) :
    produto = dict(

    nome_prod = str(input('Digite o nome do produto: ')).upper().strip(),
    nomefunc = str(input('Digite nome funcionario: ')).title().strip(),
    preço = float(input('Digite o Preço do Produto: ')),
    dt_hr = datetime.now().strftime('%d/%m/%Y - %H:%M')
    )
    estoque.append(produto)


print('\n\n')


for item in estoque:
    for chave,valor in item .items():
        print(f'{chave}->{valor}')
    print()