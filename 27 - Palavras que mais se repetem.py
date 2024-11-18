from collections import Counter

def contar_palavras_frequentes(texto):
    # Converte o texto para minúsculas e remove pontuação básica
    texto = texto.lower()
    for char in ".,!?;:":
        texto = texto.replace(char, "")
    
    # Divide o texto em palavras
    palavras = texto.split()
    
    # Conta a frequência de cada palavra
    contador = Counter(palavras)
    
    # Obtém as 5 palavras mais frequentes
    palavras_mais_frequentes = contador.most_common(5)
    
    return palavras_mais_frequentes

# Solicita ao usuário que digite um texto longo
texto_usuario = input("Digite um texto longo: ")

resultado = contar_palavras_frequentes(texto_usuario)

print("As 5 palavras mais frequentes são:")
for palavra, frequencia in resultado:
    print(f"{palavra}: {frequencia} vezes")
