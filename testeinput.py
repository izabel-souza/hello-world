a = int(input())
b = int(input())
escolha = input()
resultado = 0

if escolha == "soma":
    resultado = a + b
elif escolha == "subtracao":
    if a > b:
        resultado = a - b
    else: 
        resultado = b - a
elif escolha == "multplicacao":
    resultado = a * b
elif escolha == "divisao":
    if a > b:
        resultado = a // b
    else:
        b // a

print(resultado)