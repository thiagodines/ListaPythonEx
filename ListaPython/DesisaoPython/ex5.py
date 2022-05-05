"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = int(input('Type a grade: '))
nota2 = int(input('Type a grade: '))
media = (nota1 + nota2) / 2
print('-'*100)
print(media)
if media < 7:
    print('Disapproved!')
elif media == 10:
    print('Approved with excellence!')
else:
    print('Approved!')



