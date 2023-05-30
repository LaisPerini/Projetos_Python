"""
IF, ELSE, ELIF
Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Sintaxe:

if (teste):
    Bloco que será executado se o teste retornar True
"""

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''



# Condição simples
#numero = 10
#if numero > 5 :
    #print('10 é maior que 5')

#numero = 11
#if numero % 2 == 0 :
#    print('numero é par') 
#else:
#    print('numero impar') 


# Condição composta
#media = float(input('Media: '))

#if (media >= 7.0) and (media<=10):
   # print('Aprovado')
#elif (media>=5) and (media<7.0):
 #   print('Recuperação')
#elif (media>=0) and (media<5):
 #   print('Reprovado')     
#else:
 #   print('Média Invalida')    
    
# Condição aninhada

#idade = int(input('idade: '))

#if (idade >=18) and (idade <=65):
#    print('Pode Iniciar')
#elif (idade>=16) and (idade<18) :
 #   resposta: str(input('você tem autorização [S OU N ]')).upper()

 #   if resposta == 'S':
 #       print('podemos iniciar')
  #  elif resposta == 'N':
 #       print('podemos iniciar')
 #   else: 
  #      print('não podemos inciar ')

#elif (idade<=0) and (idade<16):
 #   print('Não pode Iniciar')  
#else:
#    ('Idade invalido')  


# Operadores unitários >>> Dependem de um único valor >>> not, is

numero=10
if not numero>5:
    print('')


# Operadores binários >>> Dependem de mais que 1 valor >>> and, or




