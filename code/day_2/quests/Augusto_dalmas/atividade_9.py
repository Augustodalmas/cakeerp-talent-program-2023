#9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []

for x in range(3):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)

numeros.sort()

print(numeros)