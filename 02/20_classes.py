"""
Uma classe é um modelo ou blueprint que descreve os atributos (variáveis) 
e comportamentos (métodos) comuns a um grupo de objetos relacionados. 

No contexto da orientação a objetos, uma classe funciona como uma base 
para criar instâncias, chamadas de objetos. Cada objeto criado a partir 
de uma classe possui os atributos e métodos definidos pela classe, 
mas com valores e estados específicos. 
"""

# Criar uma classe cliente 

class Cliente:

    def __init__(self,nome,cpf,rg):
        self._nome = nome
        self._cpf = cpf
        self._rg = rg           #self é = private

    def getNome(self):                        #metodo para imiprimir os nomes que estavam privados
        print (f'Nome: {self._nome}')
    



usuario = Cliente('Lais',123,456) 
usuario.getNome()       
print(usuario)


