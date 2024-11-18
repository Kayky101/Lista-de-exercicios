print("SEQUÊNCIA DE NÚMEROS FIBONACCI")

def seq(n):
    if n <= 0:
        return[]
    elif n == 1:
        return[0]
    elif n == 2:
        return[0, 1]
    
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        prox_num = fibonacci[-1] + fibonacci [-2]
        fibonacci.append(prox_num)

    return fibonacci
    
n = int(input("Digite quantos números você quer que apareça na Sequência a seguir: "))
fibo = seq(n)

print("Os primeiros {n} números da sequência em que escolheu são: ",fibo)
    
    



    