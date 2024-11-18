def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primos_no_intervalo(inicio, fim):
    lista_primos = []
    for i in range(inicio, fim + 1):
        if eh_primo(i):
            lista_primos.append(i)
    return lista_primos

inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

lista_primos = primos_no_intervalo(inicio, fim)

print("Os números primos no intervalo são:", lista_primos)









            