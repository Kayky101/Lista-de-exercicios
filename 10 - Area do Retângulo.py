print("Calcularemos a area de um retângulo com os valores que você, usuário, indicar.")

def calculo(base, altura):
    return base * altura / 2

altura = float(input("Indique a altura do retângulo em questão (em cm): "))
base = float(input("Agora me indique sua base e o resultado aparecerá logo em seguida (em cm): "))
resultado = calculo(altura, base)

print("A área do retângulo em questão é de:", resultado)

