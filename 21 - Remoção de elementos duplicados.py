def remover_duplicados(lista):
    nova_lista = []
    for numero in lista:
        if numero not in nova_lista:
            nova_lista.append(numero)
    return nova_lista

elementos = input("Digite uma lista de números, separados por vírgulas: ")
lista = [int(x) for x in elementos.split(",")]

resultado = remover_duplicados(lista)

print("Lista sem duplicados:", resultado)