# Conta elementos não repetidos de uma lista
# 13/1/2026


def count_non_repeat_elem(lista):
    count = 0
    n = len(lista)
    for i in range(n):
        repetido = False
        for j in range(n):
            if lista[i] == lista[j] and i != j:
                repetido = True
                break
        if not repetido:
            count += 1
    return count


if __name__ == "__main__":
    a = [1, 3, 5, 7, 3, 7, 6, 6, 4, 2, 9]
    res = count_non_repeat_elem(a)
    print(f"Elementos não repetidos: {res}")
