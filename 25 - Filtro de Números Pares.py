print("Filtro de Números Pares")

def filtrar_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

elementos = input("Digite uma lista de números, separados por vírgulas: ")
lista1 = [int(x) for x in elementos.split(",")]

resultado = filtrar_pares(lista1)

print("Lista de números pares:", resultado)

    