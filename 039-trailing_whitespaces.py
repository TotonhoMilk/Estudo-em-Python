# Tira caracteres no final da string.
# 17/1/2026


def trailing(s):
    # count = len(s) - 1
    # while s[count] == ' ' or s[count] == '\n' or s[count] == '\t':
    # count -= 1
    # return s[:count + 1]
    fim = len(s) - 1
    while fim >= 0 and s[fim] in " \n\t":
        fim -= 1
    return s[: fim + 1]


if __name__ == "__main__":
    s = "This is the way.  \n\n\t  "
    print(f"Antes:\n{s}")
    res = trailing(s)
    print(f"Depois:\n{res}")

