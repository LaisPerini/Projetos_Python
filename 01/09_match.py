"""
Estrutura condicionais mais utilizada em menus,
funciona semelhante ao escolhaCaso do portugol
e switch case no java por exemplo...
"""
n1= int(input('Digite o Primeiro Numero:'))
n2= int(input('Digite o Segundo Numero:'))
menu = int(input('''
MENU
[1] SOMAR
[2] SUBTRAIR
[3] MULTIPLICAR
[4] DIVIDIR
OPÇÃO:  '''))



match menu: 
    case 1:
        resultado = n1+n2
    case 2:
        resultado = n1-n2
    case 3:
        resultado = n1*n2
    case 4: 
        resultado = n1//n2
    case _:                              # ele é como se fosse o else 
        print('Opção Invalida')
print(f'resultado: {resultado}') 


'''

