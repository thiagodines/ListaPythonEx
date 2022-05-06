"""
Faça um Programa que leia três números e mostre o maior e o menor deles. 
"""

num_1 = input('Type the first number: ')
num_2 = input('Type the second number: ')
num_3 = input('Type the third number: ')

if not num_1.isnumeric and num_2.isnumeric and num_3.isnumeric:
    print('Type only numbers!!')

if num_1 > num_2 and num_1 > num_3:
    bigger = num_1
elif num_2 > num_1 and num_2 > num_3:
    bigger = num_2
else:
    num_3 = bigger

if num_1 < num_2 and num_1 < num_3:
    lower = num_1
elif num_2 < num_1 and num_2 < num_3:
    lower = num_2
else:
    lower = num_3

print(f'The biggiest number is {bigger}')
print(f'The lowest number is {lower}')
