"""
Senha fixa
"""
senha = int(input('Digite a senha (SOMENTE NÚMEROS): '))

while not senha == 2022:
    print('Senha invalida! Tente novamente!')
    senha = int(input('Digite a senha novamente: '))

print(f'A senha {senha} esta correta!')
