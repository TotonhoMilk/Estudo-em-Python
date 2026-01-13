# Rotação da lista para direita
# O último elemento vira o primeiro
# 13/1/2026


def rotate_list_right(lista: list[int], n):
    temp = lista[n - 1]
    for i in range(n - 2, -1, -1):
        lista[i + 1] = lista[i]
    lista[0] = temp


if __name__ == "__main__":
    a = [3, 9, 8, 1, 7, 6]
    n = len(a)
    print(a)
    print("-" * 18)
    for i in range(n):
        rotate_list_right(a, n)
        print(a)
        print("-" * 18)
