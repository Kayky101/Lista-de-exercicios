print("Verificador de Anagrama")

def anagrama(palavra1, palavra2):
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    if palavra1 == palavra2:
        return "Estas palavras são iguais, tente inserir palavras diferentes."
    elif sorted(palavra1) == sorted(palavra2):
        return "As palavras digitadas são anagramas."
    else:
        return "As palavras digitadas não são anagramas."
        
p1 = input("Agora você irá digitar duas palavras para verificarmos se são anagramas, digite a primeira palavra: ")
p2 = input("Por fim digite a segunda palavra: ")
resultado = anagrama(p1, p2)

print(resultado)