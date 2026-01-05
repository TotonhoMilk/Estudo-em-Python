# Mescla duas listas elemento por elemento.
# 5/1/2026


def merge_listas(a1, a2):
    size = len(a1) + len(a2)
    res = [0] * size
    cont = 0
    for i in range(0, size, 2):
        res[i] = a1[cont]
        res[i + 1] = a2[cont]
        cont += 1
    return res


if __name__ == "__main__":
    a1 = [1, 3, 5, 7, 9]
    a2 = [2, 4, 5, 6, 8]
    r = merge_listas(a1, a2)
    print(r)
