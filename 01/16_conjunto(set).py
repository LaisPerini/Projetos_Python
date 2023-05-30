# Sets --> Conjuntos (NÃO POSSO TER VALORES REPETIDOS)

# criando um set
dicionario1 = {'chave':'valor'}
dicionario2 = dict()

conjunto1 = {'lais',10,19.8,True}
conjunto2 = set()

# convertendo dados em sets
dados = [1,1,1,1,1,1,8,9,6,8,8]
conjunto3 = set(dados)

# Mostrando alguns métodos que funcionam com SETś
conjunto4 = {1,2,3,'lais'}

# Inserir
conjunto4.add(6)

# Remover
conjunto4.pop()
conjunto4.remove('lais')  # se esse valor não existir, vai dar erro
conjunto4.discard('lais') # não gera erro caso o valor nao exista
#conjunto4.clear()

from collections import Counter

# Analise cidades (cada pessoa que entrou colocou a cidade de nascimento)
cidade = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina',
          'Salvador','Juiz de Fora', 'Rio de Janeiro', 'Petrolina',
          'Salvador', 'São Paulo', 'São Paulo', 'São Paulo',  'Juiz de Fora',
          'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador',
          'Juiz de Fora',  'Petrolina', 'Salvador', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo',
          'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro',  'São Paulo', 'Rio de Janeiro',
          'São Paulo', 'Rio de Janeiro', 'São Paulo']

# validando quantas vezes o elemento 'Rio de Janeiro" foi inserido na lista
soma_rj = 0
for c in cidade :
    if c == 'Rio de Janeiro':
        soma_rj +=1
        
print(f'Total de Pessoas do RJ:{soma_rj}')   
print(f'Total de Pessoas do RJ:{cidade.count("Rio de Janeiro")}')     #melhor jeito de fazer 


# Como o set não repete o mesmo item, aqui podemos pegar cada um q foi inserido
cidade_hoje = set(cidade)
print(f'cidades que vieram hoje:{cidade_hoje}')

# Total de cidades que vieram hoje
print(f'cidades que vieram hoje:{len(cidade_hoje)}')

print(Counter(cidade))                    #ele conta todas os nomes das cidades 
print(Counter(cidade).most_common(3))     #most_common traz os nomes que mais se repetiu


# Análise de dados com Sets
cursoPy = ['Leonardo A.', 'Maria', 'Juca', 'Alfredo', 'Leonardo B.',
           'Alfredo', 'Guilhermina', 'Amanda', 'João', 'Pedro']

cursoBD = ['Leonardo A.', 'Beto', 'Joana', 'Maria', 'Felipe', 'Juca',
           'Leopoldo', 'Alfredo', 'Jubileu']

# Convertendo dados para Sets
py_set = set(cursoPy)
bd_set = set(cursoBD)


# Total de alunos de Python
print(f' Total de alunos de Python: {len(py_set)}') 
# Total de Alunos de BD
print(f' Total de alunos de Banco de dados: {len(bd_set)}') 
# Total de alunos da escola
print(f' Total de alunos da escola: {len(py_set.union(cursoBD))}') 

# Alunos que fazem apenas 1 curso
aluno_1_curso_py = py_set.difference(bd_set)
print(f' Total Alunos que fazem apenas 1 curso py: {len((alunos_1_curso_py))}') 

alunos_1_curso_py = bd_set.difference(py_set)
print(f' Total Alunos que fazem apenas 1 curso bd: {len((alunos_1_curso_py))}') 

ambos = py_set.intersection(bd_set)
ambos = py_set & bd_set

# Alunos que fazem os 2 cursos

# Alunos que fazem somente Python

