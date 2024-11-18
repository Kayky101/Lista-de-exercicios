print("Este é um conversor de temperatura, iremos converter graus Celcius para Farenheits.")

def convert(Celcius):
    return Celcius * 1.8 + 32

Cel = float(input ("Indique a temperatura em graus Celcius que você deseja converter: "))

resultado = convert(Cel)

print("Esta temperatura em grau Celcius (°C) se converte em:", resultado, "°F")