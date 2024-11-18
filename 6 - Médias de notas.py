def calcular_media(nota1, nota2, nota3):
    resultado = (nota1 + nota2 + nota3)
    media = resultado / 3
    return round(media, 2)

def result(media):
    if 0 <= media < 6:
        return f"Sua média é: {media}. Que pena, você precisa se esforçar mais. :("
    elif 6 <= media <= 10:
        return f"Sua média é: {media}. Parabéns!! Você passou!!"
    else:
        return "Você não inseriu notas válidas."

nota1 = float(input("Me diga suas últimas 3 notas para que possamos fazer uma média, começando pela primeira: "))
nota2 = float(input("Agora indique sua segunda nota: "))
nota3 = float(input("Por fim me fale sua terceira e última nota: "))

media_arredondada = calcular_media(nota1, nota2, nota3)

resultado = result(media_arredondada)

print(resultado)


