print("Contagem de Vogais e Consoantes")

def contar_vogais_consoantes(frase):
    vogais = "aeiouAEIOU"
    contagem = {"vogais": 0, "consoantes": 0}
    
    for caractere in frase:
        if caractere.isalpha():  
            if caractere in vogais:
                contagem["vogais"] += 1
            else:
                contagem["consoantes"] += 1
                
    return contagem

usuario = input("Digite a frase que você deseja ver a quantidade de vogais e consoantes respectivamente: ")

resultado = contar_vogais_consoantes(usuario)

print("Contagem de vogais e consoantes:", resultado)
