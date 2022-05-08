"""
Faça um Programa que leia três números e mostre o maior e o menor deles. 
"""

num_1 = int(input('Type the first number: '))
num_2 = int(input('Type the second number: '))
num_3 = int(input('Type the third number: '))

# Maior número:
maior = num_1
if num_2 > maior:
    maior = num_2

if num_3 > maior:
    maior = num_3

# Menor número:
menor = num_1
if num_2 < menor:
    menor = num_2

if num_3 < menor:
    menor = num_3


print(f'The biggiest number is {maior}')
print(f'The lowest number is {menor}')
