nome = str(input('Nome: ')).title()
idade = int(input('Idade:'))
peso = float(input('Peso:'))
altura = float(input('Altura:'))

#Retorne o IMC do usuário.

IMC =   peso/altura ** 2

print(IMC)
print(f'Seu imc:{IMC:.2f}')






