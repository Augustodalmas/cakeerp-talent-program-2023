"""7 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

sexo = input("Digite F para Feminino ou M para masculino\n")

if sexo == 'F':
    print("sexo válido, Feminino")
elif sexo == 'M':
    print("sexo válido, Masculino")
else:
    print("sexo Inválido")