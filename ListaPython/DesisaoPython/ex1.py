"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

if not num_1.isnumeric() or not num_2.isnumeric():
    print('Você deve digitar um número valido!')
else:
    if num_1 < num_2:
        print(f'O {num_1} é menor que {num_2}')
    else:
        print(f'O {num_2} é menor do que {num_1}')



