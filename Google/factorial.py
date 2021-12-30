def fatorial(n):
    result = 1
    for i in range(n):
        result += result * i
    print(result)

fatorial(5)
