# Roração de lista.
# O primeiro elemento vira o último.
# 5/1/2026


def rotate_lista(lista: list[int], n):
    temp = lista[0]
    for i in range(n - 1):
        lista[i] = lista[i + 1]
    lista[n - 1] = temp


if __name__ == "__main__":
    a = [3, 9, 8, 1, 7, 6]
    n = len(a)
    print(a)
    print("-" * 18)
    for i in range(n):
        rotate_lista(a, n)
        print(a)
        print("-" * 18)
