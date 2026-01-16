# Bubble-sort.
# 16/1/2026


def bubble_sort1(lista):
    sort = True
    n = len(lista)
    passes = 1
    while sort:
        swap = False
        print(f"Passo {passes}:")
        for i in range(n - 1):
            print(f"a[{i}] > a[{i + 1}] --> {lista[i]} > {lista[i + 1]}")
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
                swap = True
                print(f"\tTrue --> Swap {lista[i]} <-> {lista[i + 1]}")
        passes += 1
        if not swap:
            break


def bubble_sort2(lista):
    n = len(lista)
    for i in range(n - 1):
        print(f"Passo {i + 1}:")
        for j in range(n - i - 1):
            print(f"a[{j}] > a[{j + 1}] --> {lista[j]} > {lista[j + 1]}")
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                print(f"\tTrue --> Swap {lista[j]} <-> {lista[j + 1]}")


if __name__ == "__main__":
    a1 = [5, 1, 4, 2, 8]
    a2 = [5, 1, 4, 2, 8]
    print(a1)
    bubble_sort1(a1)
    print(a1)
    print("\n=====================\n")
    print(a2)
    bubble_sort2(a2)
    print(a2)
