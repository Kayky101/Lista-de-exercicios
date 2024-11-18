print("Verificação de Maioridade")

def verificar_maioridade(idade):
    if idade < 18:
        return "Você é menor de idade !!! Por favor, não beba bebidas alcoólicas."
    elif idade >= 18:
        return "Você é maior de idade !!! Pode beber, mas apenas com responsabilidade."

age = int(input("Digite a sua idade, e verificaremos se você é maior de idade ou não: "))

resultado = verificar_maioridade(age)

print(resultado)
