def sequencia_fibonacci(n):
    if n <=0:
        return[]
    elif n ==1:
        return [0]
    elif n ==2:
        return [0,1]
    else:
        sequencia= sequencia_fibonacci(n -1)
        next_numero = sequencia[-1]+ sequencia[-2]
        sequencia.append(next_numero)
        return sequencia
    
n = int(input('Informe um numero inteiro:'))
resultado = sequencia_fibonacci(n)
print(resultado)