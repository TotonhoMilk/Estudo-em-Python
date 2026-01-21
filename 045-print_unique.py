# Imprime apenas caracteres não repetidos
# 21/1/2026


def printUnique(a):
    n = len(a)
    for i in range(n):
        match = False
        for j in range(n):
            if a[i] == a[j] and i != j:
                match = True
        if not match:
            print(f"{a[i]}", end=" ")


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 3, 4, 1, 8, 9, 7, 8]
    printUnique(a)

