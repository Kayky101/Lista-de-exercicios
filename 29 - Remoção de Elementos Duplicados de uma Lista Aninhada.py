def remover_duplicados_lista_aninhada(lista_aninhada):
    nova_lista_aninhada = []
    for sublista in lista_aninhada:
        nova_sublista = []
        for item in sublista:
            if item not in nova_sublista:
                nova_sublista.append(item)
        nova_lista_aninhada.append(nova_sublista)
    return nova_lista_aninhada

# Solicitar a lista aninhada do usuário
print("Digite a lista aninhada. Para cada sublista, digite os números separados por vírgula. Digite 'fim' para terminar.")

lista_aninhada = []
while True:
    entrada = input("Digite uma sublista ou 'fim' para terminar: ")
    if entrada.lower() == "fim":
        break
    sublista = list(map(int, entrada.split(",")))
    lista_aninhada.append(sublista)

resultado = remover_duplicados_lista_aninhada(lista_aninhada)
print("Lista aninhada sem duplicados:", resultado)
