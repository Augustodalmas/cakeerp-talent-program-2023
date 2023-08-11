#6 - Faça um Programa que peça dois números e imprima o maior deles.

valor = []
maior = 0
for x in range(2):
    valor = int(input("Digite um valor: "))
    if valor > maior:
        maior = valor

print("O maior numero digitado foi: " +str(maior))