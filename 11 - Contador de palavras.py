print("Agora você está diante de um contador de palavras.")

def contf(lista):
    palavra = lista.split(" ")
    return len(palavra)

frase = input("Escreva uma frase para que o programa possa contar quantas palavras ela tem: ")

resultado = contf(frase)

print("O número de palavras desta frase é:", resultado)