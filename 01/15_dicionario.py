"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}
exemplo2 = dict()

Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""

# criando dicionários

tupla1 = ()
tupla2 = tuple()

lista1= ['lais']
lista2 = list()

dicionario = {}
dicionario2 = dict()

dicionario3 = {'chave' : 'valor'}
dicionario4 = {'idade': 30, 'cpf' : 452085788, 'rg' : 48050224}

dicionario5 = dict(idade=30,cpf=4520857808,rg=48050224)

# buscar
paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'py': 'Paraguai'
}

resp = str(input('Digite a sigla: ')).lower().strip()    #strip remove espaços da linha digitado

# busca menos usual (erro caso não encontre a chave)
print(f'Encontrei: {paises[resp]}')
print(f'Encontrei: {paises.get(resp,"Ops, não encontrei")}') # se abrir com aspas simples, e precisar colocar como texto dentro ai teria que colocar aspas duplas



# busca mais usual


# Inserir, remover, atualizar
receita = {
    'JAN': 2.000,
    'FEV': 4.000,
    'MAR': 8.000
}

#inserir
receita['ABR'] = 10000
print(receita)

#atualizar 
receita.update({'DEZ': 90000})
print(receita)

#remover
receita.pop('JAN') #remove o valor passando a chave 
receita.popitem() # remove a ultima chave e valor
print(receita)

print(receita.keys()) # imprime todos as chaves
print(receita.values()) #imprime todos os valor

for chave,valor in receita.items(): #pra pegar os valores precisa por items
    print(f'Na chave {chave}, temos o valor:{valor}')







