def pertence_fibonacci(numero):
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return "Pertence à sequência de Fibonacci"
        a, b = b, a + b
    return "Não pertence à sequência de Fibonacci"

# Teste
numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))
