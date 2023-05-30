"""  
HERANÇA é um tipo de relacionamento entre classes 
que significa que uma classe é outra.

POLIMORFISMO é a capacidade que uma subclasse tem de 
ter métodos com o mesmo nome de sua superclasse, e o 
programa saber qual método deve ser invocado, 
especificamente (da super ou sub). 
"""

class Pessoa:
    def __init__(self,nome,cpf,rg):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg 

    def getAll(self):
        return [self.__nome,self.__cpf,self.__rg]
    

class Cliente:
    def __init__(self,nome,cpf,rg,tel):
        super().__ini__(nome,cpf,rg)
        self.__tel = tel        

    def getNome(self):                        
        print (f'Nome: {self.__nome}')


class Funcionario:
    def __init__(self,nome,cpf,rg,matricula):
        Pessoa.__init__(self,nome,cpf,rg)
        self.__matricula = matricula     

    def getAll(self):
        return [self._Pessoa__nome,self._Pessoa__cpf,self._Pessoa__rg,self.__matricula]
    

a = Cliente('Leo',13,134,89)
print(a.getAll())   

b = Funcionario('Leo',13,134,89)
print(b.getAll())    
    