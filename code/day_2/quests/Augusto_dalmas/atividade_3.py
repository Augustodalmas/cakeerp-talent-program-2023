"""
3 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A. "Telefonou para a vítima?"
B. "Esteve no local do crime?"
C. "Mora perto da vítima?"
D. "Devia para a vítima?"
E. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

perguntas = ("Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?")
classificacao = 0

for pergunta in perguntas:
    print(pergunta)
    resposta = int(input("1=True\n2=False\n"))
    if resposta == 1:
        classificacao += 1

print(classificacao)

if classificacao == 2:
    print('Voce e Suspeito!')
elif classificacao >= 3 and classificacao <= 4:
    print('Voce e Cúmplice!')
elif classificacao == 5:
    print("Achamos o Assasino!")
else:
    print("Voce e inocente!")