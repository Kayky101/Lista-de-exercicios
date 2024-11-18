print("VERIFICADOR DE NÚMERO PAR OU ÍMPAR!!")

def verificador(numero):
    if numero % 2:
        return "Ímpar"
    else:
        return "Par"

num1 = int(input("Digite um número que o programa irá dizer se é Par ou Ímpar: "))
resultado = verificador(num1)

print(f"O seu número é {resultado}.")
