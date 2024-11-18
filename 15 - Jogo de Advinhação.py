print("JOGO DA ADIVINHAÇÃO")

import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Tente adivinhar o número que eu pensei, de 1 a 100: "))
    tentativas +=1
    
    if chute < numero_secreto:
        print("O número que eu pensei é MAIOR que este último chute.")
    elif chute > numero_secreto:
        print("O número que eu pensei é MENOR que este último chute.")
    else:
        print("Parabéns! Você adivinhou o número!")
        print("O número de tentativas usadas foi:", tentativas)

    


