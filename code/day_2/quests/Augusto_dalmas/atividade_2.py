"""2 - Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida."""

idades = []
alturas = []

for x in range(5):
    idades.append(input("Digite sua idade: "))
    alturas.append(input("Digite sua Altura: "))

print("\nA ordem original do vetor Idades é")
print(idades)
print("\nA ordem Original do vetor altura é")
print(alturas)

idades.reverse()
alturas.reverse()

print("\nA ordem invertida do vetor Idades é")
print(idades)
print("\nA ordem invertida do vetor altura é")
print(alturas)