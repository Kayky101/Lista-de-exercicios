print("VERIFICADOR DE PALÍNDROMOS.")

palavra = input("Digite a palavra que deseja verificar se é um palíndromo ou não: ")

def palindromo(palavra):
    if palavra == palavra [::-1]:
        print("A sua palavra é um palíndromo.")
    else:
        print("A sua palavra não é um palíndromo.")

resultado = palindromo(palavra)