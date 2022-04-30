"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome = input('Digite seu Login: ')
senha = input('Digite sua senha: ')

while nome == senha:
    print()
    print('LOGIN E SENHA NÃO PODEM SER IGUAIS.')
    nome = input('Digite seu Login: ')
    senha = input('Digite sua senha: ')
print()
print(f'Login: {nome}')
print(f'Senha: {senha}')


