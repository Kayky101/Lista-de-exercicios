
def soma_diagonais(matriz):
    n = len(matriz)
    soma_principal = sum(matriz[i][i] for i in range(n))
    soma_secundaria = sum(matriz[i][n - 1 - i] for i in range(n))
    return soma_principal, soma_secundaria

n = int(input("Digite a dimensão da matriz quadrada (n x n): "))

matriz = []
print("Digite os elementos da matriz, linha por linha (utilizando espaços):")
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

print("Matriz inserida:")
for linha in matriz:
    print(linha)

soma_principal, soma_secundaria = soma_diagonais(matriz)

print("Soma da diagonal principal:", soma_principal)
print("Soma da diagonal secundária:", soma_secundaria)
