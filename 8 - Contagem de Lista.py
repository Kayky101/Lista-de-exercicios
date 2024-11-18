def contar_numeros(lista):
    numeros = lista.replace(" ", "").split(",")
    return len(numeros)

lista = input("Digite uma lista de números, separando por vírgula, que o programa indicará quantos números ela tem: ")

contagem = contar_numeros(lista)

print("A sua lista tem:", contagem, "números.")
