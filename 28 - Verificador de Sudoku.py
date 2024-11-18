def verificar_conjunto(conjunto):
    numeros = [num for num in conjunto if num != 0]
    return len(numeros) == len(set(numeros)) and all(1 <= num <= 9 for num in numeros)

def verificar_sudoku(tabuleiro):
    for linha in tabuleiro:
        if not verificar_conjunto(linha):
            return False

    for coluna in range(9):
        coluna_valores = [tabuleiro[linha][coluna] for linha in range(9)]
        if not verificar_conjunto(coluna_valores):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrade = []
            for x in range(3):
                for y in range(3):
                    subgrade.append(tabuleiro[i + x][j + y])
            if not verificar_conjunto(subgrade):
                return False

    return True

print("Digite o tabuleiro de Sudoku linha por linha, com os números separados por espaço. Use 0 para espaços vazios.")
tabuleiro_usuario = []
for _ in range(9):
    linha = list(map(int, input("Digite uma linha do tabuleiro: ").split()))
    tabuleiro_usuario.append(linha)

resultado = verificar_sudoku(tabuleiro_usuario)
print("O tabuleiro de Sudoku é válido?", resultado)



