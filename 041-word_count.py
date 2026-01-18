# Conta quantas palavras tem na string
# 17/1/2026


def word_count(s):
    n = len(s)
    count = 0
    in_word = False
    for i in range(n):
        if s[i] not in " ,.:!?\n\t":
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count


if __name__ == "__main__":
    s = "This is, the way.  Another..."
    r = word_count(s)
    print(f"Total de {r} palavras")
