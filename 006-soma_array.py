# Soma os elementos de uma matriz
# 23/12/2025

def sumArrayValues(numbers:list[int]) -> int:
    soma = 0
    for num in numbers:
        print(f"soma = {soma:2d} + {num:2d}")
        soma += num
    return soma

if __name__ == '__main__':
    test_array = [1,2,3,4,5,6]
    somaVal = sumArrayValues(test_array)
    print(f"A soma dos elementos da matriz é: {somaVal}")
