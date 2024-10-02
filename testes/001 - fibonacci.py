def fibonacci(n):
    if n < 0:
        return print("Número inválido!")

    a, b = 0, 1

    while a <= n:
        if a == n:
            return print(
                "O número informado faz parte da sequencia de fibonacci.")
        a, b = b, a + b

    return print("O número informado não faz parte da sequencia de fibonacci.")


num = int(input("Informe um número: "))
fibonacci(num)
