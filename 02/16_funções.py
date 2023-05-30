"""
FUNÇÔES
Uma forma de organizar o código e garantir que ele 
possa ser reutilizado. Ideal que cada função seja 
responsável por uma tarefa...
"""
#ENTRAR NA PASTA 02 TEM QUE COLOCAR CD 02(NOME DA PASTA) .. SEGUINDO COM PYTHON E NOME DA PASTA

#função diz oi


def dizOi():
    print('Oi')

dizOi()

#função canta parabéns

def parabens():
    print('parabéns pra você')

parabens()


#função soma 2 valores
def soma2():
    numeros = []
    for n in range(2):
        numeros.append(int(input(f'Digite o {n+1} numero: ')))
    print(f'somando os valores, temos: {sum(numeros)}')

soma2()






