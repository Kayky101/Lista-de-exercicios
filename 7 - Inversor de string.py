def palavra(words):
    return words [::-1] 
    
word = input("Digite uma palavra que deseja ver invertida: ")
palavra_invertida = palavra(word)

print("A palavra invertida é:", palavra_invertida)