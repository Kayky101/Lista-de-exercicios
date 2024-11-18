print("O programa irá contar a quantidade de cada caractére de uma frase.")

def contadorf(frase):
    contagem = {}
    for caractere in frase:
        if caractere in contagem:
            contagem[caractere] += 1
        else: 
            contagem[caractere] = 1
    return contagem
    

frase = input("Insira a frase em que quer que contemos os caractéres: ")

resultado = contadorf(frase)

print("A contagem de caractéres é:")
for caractere, contagem in resultado.items():
    print(f"{caractere} : {contagem} vezes")