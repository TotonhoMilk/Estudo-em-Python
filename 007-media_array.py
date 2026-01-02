# Calcula a média dos elementos da matriz
# 23/12/2025

def avaregeList(numbers:list[float]) -> float:
    soma = 0.0
    for num in numbers:
        print(f"Soma = {soma:.2f} + {num:.2f}")
        soma += num
    print(f"Média = {soma:.2f} / {len(numbers)}")
    return soma / len(numbers)

if __name__ == '__main__':
    test_array = [1,2,3,4,5,6,7,8]
    media = avaregeList(test_array)
    print(f"A média dos valores é: {media:.2f}")
