# Remove todos caracteres iguais de uma string
# 28/12/2025


def remove_char(str, c):
    n = len(str)
    print(f"Remover a letra {c} da palavra {str}")
    print(f"Tamanho da string: {n}\n")
    res = ""
    for letra in str:
        print(f"Se {letra} == {c} -> {letra == c}")
        if letra == c:
            print("\tContinue")
            continue
        res += letra
        print(f"\tres += letra: {letra}")
    print(f"\n\tResultado: {res}")


if __name__ == "__main__":
    s = "banana"
    c = "a"
    remove_char(s, c)
