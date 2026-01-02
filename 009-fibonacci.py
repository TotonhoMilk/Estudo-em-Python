# Escreve a sequencia de Fibonacci recursivamente
# 23/12/2025

def fib(num:int) -> int:
    if num == 0:
        return 1
    if num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)

if __name__ == '__main__':
    for i in range(30):
        resultado = fib(i)
        print(f"{resultado} ", end='')
