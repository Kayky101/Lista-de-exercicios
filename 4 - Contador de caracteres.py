print("Agora o programa irá indicar a quantidades de caractéres da palavra escolhida pelo usúario:")

def contador(word):
    return len(word)

palavra = (input("Digite a palavra em que está pensando: "))
resultado = contador(palavra)

print("O número de caractéres da sua palavra é:", resultado)