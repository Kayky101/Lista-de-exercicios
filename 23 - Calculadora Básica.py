print("CALCULADORA.")

def calculator(n1, operador, n2):
    if operador == "+":
        return n1 + n2
    elif operador == "-":
        return n1 - n2
    elif operador == "*":
        return n1 * n2
    elif operador == "/":
        return n1 / n2
    
n1 = float(input("Indique o primeiro número da sua operação: "))
operador = input("Agora digite o operador que deseja utilizar: ")
n2 = float(input("Por fim indique o número que completará a operação: "))

resultado = calculator(n1, operador, n2)
print(resultado)
    

    