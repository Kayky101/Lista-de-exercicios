def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def notas_maiores_que_media(notas):
    media = calcular_media(notas)
    notas_maiores = [nota for nota in notas if nota > media]
    return notas_maiores

notas = input("Digite as notas dos alunos separadas por vírgula: ")
notas = [float(nota) for nota in notas.split(",")]

notas_maiores = notas_maiores_que_media(notas)

print("A média das notas é:", calcular_media(notas))
print("As notas maiores que a média são:", notas_maiores)






