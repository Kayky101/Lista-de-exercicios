def mesclar_dicionarios(dic1, dic2):
    for chave in dic2:
        if chave in dic1:
            dic1[chave] += dic2[chave]
        else:
            dic1[chave] = dic2[chave]
    return dic1

print("Digite os itens do primeiro dicionário no formato chave:valor (por exemplo, a:1)")
dicionario1 = {}
while True:
    entrada = input("Digite a chave e o valor separados por dois pontos (ou pressione Enter para terminar): ")
    if entrada == "":
        break
    chave, valor = entrada.split(":")
    dicionario1[chave.strip()] = int(valor.strip())

print("Digite os itens do segundo dicionário no formato chave:valor (por exemplo, b:2)")
dicionario2 = {}
while True:
    entrada = input("Digite a chave e o valor separados por dois pontos (ou pressione Enter para terminar): ")
    if entrada == "":
        break
    chave, valor = entrada.split(":")
    dicionario2[chave.strip()] = int(valor.strip())

resultado = mesclar_dicionarios(dicionario1, dicionario2)
print("Dicionário mesclado:", resultado)


