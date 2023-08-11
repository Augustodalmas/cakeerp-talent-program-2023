"""
10 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
A. salários até R$ 280,00 (incluindo) : aumento de 20%
B. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
C. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
D. salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
E. o salário antes do reajuste;
F. o percentual de aumento aplicado;
G. o valor do aumento;
H. o novo salário, após o aumento.
"""

colaborador = int(input("Qual o seu sálario? "))

if colaborador <= 280:
    print("Salario antes do reajuste: ", int(colaborador))
    print("Será aplicado aumento de 20%!")
    reajuste = colaborador + (colaborador * 0.2)
    print("Salario após o reajuste: ", int(reajuste))
    print("Valor de aumento: ", (colaborador * 0.20))
elif colaborador > 280 and colaborador <= 700:
    print("Salario antes do reajuste: ", int(colaborador))
    print("Será aplicado aumento de 15%!")
    reajuste = colaborador + (colaborador * 0.15)
    print("Salario após o reajuste: ", int(reajuste))
    print("Valor de aumento: ", (colaborador * 0.15))
elif colaborador > 700 and colaborador <= 1500:
    print("Salario antes do reajuste: ", int(colaborador))
    print("Será aplicado aumento de 10%!")
    reajuste = colaborador + (colaborador * 0.10)
    print("Salario após o reajuste: ", int(reajuste))
    print("Valor de aumento: ", (colaborador * 0.10))
elif colaborador > 1500:
    print("Salario antes do reajuste: ", int(colaborador))
    print("Será aplicado aumento de 5%!")
    reajuste = colaborador + (colaborador * 0.05)
    print("Salario após o reajuste: ", int(reajuste))
    print("Valor de aumento: ", (colaborador * 0.05))
else:
    print("Valor invalido")
