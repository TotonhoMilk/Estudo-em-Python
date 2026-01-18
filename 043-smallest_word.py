# Conta o tamanho da menor palavra na string.
# 18/1/2026


def smallest_word(s):
    n = len(s)
    length = 0
    min = 10
    for i in range(n):
        if s[i] not in " .,:!?\n\t":
            length += 1
        else:
            if length > 0 and length < min:
                min = length
            length = 0
            print(f"min: {min}")
    return min


if __name__ == "__main__":
    s = "This is, the way. Again... Alexandre"
    r = smallest_word(s)
    print(s)
    print(f"A menor palavra tem {r} letras.")
