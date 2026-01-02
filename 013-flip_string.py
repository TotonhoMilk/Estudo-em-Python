# Inverte os caracteres de uma string.
# 25/12/2025


def flipLetter(str) -> str:
    return str.swapcase()


if __name__ == "__main__":
    s = "abcdeABCDE"
    print(f"String normal: {s}")
    s_invertido = flipLetter(s)
    print(f"String normal: {s_invertido}")
