# Tira caracteres no ínicio da string.
# 17/1/2026


def trim(s):
    count = 0
    while s[count] == " " or s[count] == "\n" or s[count] == "\t":
        count += 1
    return s[count:]


if __name__ == "__main__":
    s = "   \n\n\t   This is the way."
    print(f"Antes:\n{s}")
    res = trim(s)
    print(f"Depois:\n{res}")

