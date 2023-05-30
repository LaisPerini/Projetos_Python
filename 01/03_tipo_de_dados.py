'''
Python possui o que chamamos de tipagem fraca.

STRING por padrão, sempre estará entre
    ' ' aspas simples
    " " aspas duplas
    ''' ''' aspas simples triplas
    E aspas duplas trilas, como esta que cerca este comentár
'''

# string --> texto

#nome = str(input('Digite o seu nome: '))
#nome = str(input('Digite o seu nome: ')).title() # Da pra usar direto title - upper etc

#print(nome)
#print(nome.title())   # Trata a informação para o padrão com a letra maiuscula e o resto minusculo
#print(nome.upper())
#print(nome.lower())
#print(nome.capitalize()) # Trata somente a primeira letra que deixa maiuscula 
#print(nome.lower().count('a'))  # Ele conta quantas letras 'A' tem no nome, porém quando a letra for maiuscula ele conta como 1
#print(nome.lower().count('a'))  # Ele conta todas as letras 'A' tem no nome

#----------------------------------------------------------------------------------------------------------------
# Inteiro --> Int

#idade = int(input('Idade: '))

# Decimal --> FLOAT

#altura = float(input('Altura: '))
#print(altura)

#Booleano --> bool (verdadeiro ou falso)

#status = True
#status = bool(input('Situação: ')).title()

#Cadastre Nome,idade,cpf e status de um usuario: 


Nome = str(input('Digite o seu Nome: ')).title()
Idade = int(input('Digite sua Idade: '))
CPF = str(input('Digite seu CPF: ' ))
Status = True

print (Nome,Idade,CPF,Status)


# Fatiamento de String
# exemplos de métodos para string
# Metodos podem ser utilizados na mesma construção.
# Número inteiro - int | ex: 123 65 98 90
# Float >>> Números reais/ decimais separados por . e não ,
# Booleano >>> 2 constantes - Verdadeiro (True) e falso (false).



