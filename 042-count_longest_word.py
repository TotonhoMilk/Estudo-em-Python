# Conta o tamanho da maior palavra na string
# 17/1/2026


def largest_word(s):
    n = len(s)
    i = 0
    length = 0
    max = 0
    while i < n:
        if s[i] not in " .,:!?\n\t":
            length += 1
        else:
            if length > max:
                max = length
            length = 0
        i += 1
    if length > max:
        max = length
    return max


if __name__ == "__main__":
    s = "This is, the way. Again...  Alexandre"
    r = largest_word(s)
    print(f"A maior palavra tem {r} letras")
