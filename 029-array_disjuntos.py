# Verifica se os conjuntos são disjuntos.
# Conjuntos disjuntos apresentam todos os elementos diferentes entre si.
# 5/1/2026


def is_disjuntos(lista1, lista2):
    n1 = len(lista1)
    n2 = len(lista2)
    for i in range(n1):
        for j in range(n2):
            print(f"n[{i}]={lista1[i]} == n[{j}]={lista2[j]}")
            if lista1[i] == lista2[j]:
                return False
    return True


if __name__ == "__main__":
    l1 = [1, 3, 5, 7, 9]
    l2 = [2, 4, 6, 8, 10]
    if is_disjuntos(l1, l2):
        print("Os conjuntos são disjuntos!")
    else:
        print("Os conjuntos não são disjuntos!")
