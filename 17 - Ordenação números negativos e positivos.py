print("ORDENAÇÃO DE LISTA")
print("O usuário me dará uma lista de númmeros separados por vírgula, e o programa ordenará esses números em ordem CRESCENTE.")

def ordem(lista):
    list = lista.replace(" ", " ").split(",")
    return sorted(list)

numeros = input("Digite a sua lista aqui: ")

resultado = ordem(numeros)

print("Aqui está a sua lista em forma ordenada:", resultado)
