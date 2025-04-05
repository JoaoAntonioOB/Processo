def pertence_fibonacci(num):
    a, b = 0, 1
    if num == 0 or num == 1:
        return True

    while b < num:
        a, b = b, a + b

    return b == num

numero = int(input("Digite um número: "))


if pertence_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} NÃO pertence à sequência de Fibonacci.")
