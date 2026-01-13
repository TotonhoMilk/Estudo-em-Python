# Achar manualmente o valor do tamanho da string.
# 13/1/2026


def strlen(str):
    count = 0
    for char in str:
        count += 1
    return count


if __name__ == "__main__":
    s1 = "This is the way."
    print(f"Tamanho da string (len): {len(s1)}")
    print(f"Tamanho da string (strlen): {strlen(s1)}")
