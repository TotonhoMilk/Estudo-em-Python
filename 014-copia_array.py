# Cria uma cópia de um array.
# 251/12/2025


def copy_array(numbers: list[int]) -> list:
    num = numbers
    return num


if __name__ == "__main__":
    a1 = [1, 2, 3]
    a2 = [1, 2, 3, 4, 5, 6, 7]
    print("a1:")
    print(a1)
    print("Cópia de a1:")
    a1_cp = copy_array(a1)
    print(a1_cp)
    print("a2:")
    print(a2)
    a2_cp = copy_array(a2)
    print("Cópia de a2:")
    print(a2_cp)
