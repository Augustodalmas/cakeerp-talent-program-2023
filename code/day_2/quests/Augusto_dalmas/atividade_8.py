"""
8 - Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
B. A mensagem "Reprovado", se a média for menor do que sete;
C. A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

notas = []
media = 0
qtdNotas = 2

for x in range(qtdNotas):
    nota = int(input("Qual sua nota? "))
    media = media + nota

media = media/qtdNotas

if media >= 7:
    print("Parabens, voce foi aprovado com media ", str(media))
elif media < 7:
    print("Aluno Reprovado com a media: ", str(media))
elif media == 10:
    print("Aluno aprovado com distinção!")