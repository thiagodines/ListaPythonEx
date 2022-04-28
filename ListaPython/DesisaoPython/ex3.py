"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = input('Digite "M" para Masculino ou "F" para Feminino: ')

if sexo == 'm':
    print('Você é do sexo masculino!')
elif sexo == 'f':
    print('Você é do sexo Feminino!')
else:
    print('Sexo inválido!')


