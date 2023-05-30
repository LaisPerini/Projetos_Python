"""
Primeiro passo para leitura, é abrir o arquivo, para isto usamos
a função OPEN(nomeArquivo).
O parâmetro é o nome ou caminho do arquivo.

O arquivo deve existir, caso contrário retornará erro FileNotFound.

Open apenas abre o arquivo, para ler seu conteúdo é necessário usarmos
a função nomeArquivo.read()
Por padrão o Open abre com o parâmetro r(read)
"""

# criando um arquivo txt       
 with open('curso python.txt','r') as arquivo:

try:                                                            # tratamento de erro
    with open('curso python.txt','r') as arquivo:               # r significa leitura do arquivo
     print(arquivo)
     

    with open('curso python.txt','a') as arquivo:               # a ele adiciona a palavra toda vez que executar 
        arquivo.write('\nlais') 
        
    with open('curso python.csv','w') as arquivo:               # w ele cria e sobrescreve 
        arquivo.write('\nlais')                                  
                                        

except FileNotFoundError:
   with open('curso python.txt','a') as arquivo:                # ele cria o arquivo e insere o texto no caso lais
     arquivo.write('lais')

 except FileNotFoundError:                                      #tratamento do erro
 print('Não encontrei o Arquivo')   

                     
with open('curso python.txt') as arquivo:
   print(arquivo.read())                        #read ele faz a leitura do arquivo


# Exercício de aula: criar um todo (lista de tarefas)
def todo():

    while True:
        menu = int(input('[1] Inserir [2] Visualizar [3] Sair \n Opção:' ))
        match menu:
            case 1 :
                try:
                    with open('todo.txt','a', encoding = 'utf8') as arquivo:
                        while True:
                            tarefa = str(input('Digite uma Tarefa ou [s] para encerrar: '))
                            if tarefa.upper() == 'S':
                                break
                            else:
                             arquivo.write(f'{tarefa}\n')

                except FileNotFoundError:
                    print('Arquivo não encontrado')    

            case 2 :
                try:
                    with open('todo.txt','r',encoding='utf8') as doc:
                     print(doc.read())
                except FileNotFoundError:
                    print('arquivo não encontrado')               
            case 3 : 
                break
            case _:
                print('Opção Invalida')    
        
todo()        
