"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
"""


str1 = input('Digite uma palavra ou frase: ')
str2 = input('Digite uma palavra ou frase: ')

print(f'O tamanho de {str1} é de', len(str1), 'caractere.')
print(f'O tamanho de {str2} é de', len(str2), 'caractere.')

if len(str1) == len(str2):
    print('As duas strings tem a mesma quantidade de caracteres!')
else:
    print('As duas strings não possuem a mesma quantidade de caracteres!')

