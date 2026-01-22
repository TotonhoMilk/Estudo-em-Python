# Imprime a string em ordem reversa usando recursão.
# 22/1/2026


def print_reverse(s):
    if len(s) == 0:
        return
    print_reverse(s[1:])
    print(s[0], end="")


if __name__ == "__main__":
    s = "This is the way."
    print_reverse(s)
    print()
