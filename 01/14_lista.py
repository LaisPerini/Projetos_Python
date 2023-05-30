'''
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

** LIMITAÇÃO >>> Busca deve ser feita sempre por índices...
'''

tupla1 = ()
tupla2 = tuple()
lista1 = [range(11)]
lista2 = list(range(11))

nomes = {'léo','maria','Beto'}

for nome in nomes:
    print(f'Boa Noite,{nome}!')

# Sort, Reverse, Count

lista7 = [1, 5, 6, 4, 3,3, 8, 7]
print(lista7)
lista7.sort()         #sort é para aparecer na ordem crescente 
print(lista7)
lista7.reverse()      # reverse é do maior para o menor
print(lista7)
print(lista7.count(3))  #conta quantos elementos


# manipulando elementos

lista8 = [10,20]

#inserir
lista8.append(40)   #append ele insere o ultimo elemento da lista
print(lista8)

lista8.append([40,18])   #append ele insere o ultimo elemento da lista com mais numeros no caso uma tupla
print(lista8)

lista8.insert(2,25)  #insert o 2 seria a posição da lista e o 25 seria o valor pra ser inserido.
print(lista8)

#remover
lista8.pop()  #remove o ultimo elemento da lista 
print(lista8)

lista8.pop(2)  #remove o numero que estiver na posição 2
print(lista8)

lista8.remove(10) #remove o elemento, apenas o primeiro que ele encontra
print(lista8)

lista8.clear()  #limpa toda a lista
print(lista8)


# acessando índice e elemento


nomes = ['leo','maria','juca']

for indice,nome in enumerate(nomes):   #acessar é para acessar os dois
    print(f'Na posição {indice+1} ficou a pessoa: {nome}')



user = []

for u in range(3):
    user.append(str(input('digite um nome:')))
    print(user)


#copy
a= [10,20,30]
#b=a
b= a[:]                # [:] ele pega do começo ao fim se for [1:6] ele pegaria o comeco e iria ate o 6

b.append('leo')

print(f'Lista A: {a}')
print(f'Lista B: {b}')




# Inserindo elementos com for



# Desafio de aula: cadastrar quanto foi gasto nos almoços da semana:
import matplotlib.pyplot as plt  

semana = ('Seg','ter','qua','qui','sex','sab','dom')
gasto = []

for dia in semana:
    gasto.append(float(input(f'Valor gasto: [{dia}] ')))

plt.plot(semana,gasto,'r')
plt.xlabel('Dias da Semana')
plt.ylabel('Valores')
plt.show()                        




#print(sum(gasto))
#print(max(gasto))
#print(min(gasto))
#print(len(gasto)) #quantidade de itens

     


print()