# Soma N números naturais recursivamente
# 16/1/2026


def sum(n):
    if n <= 1:
        return 1
    return n + sum(n - 1)


if __name__ == "__main__":
    n = 20
    r = sum(n)
    print(f"A soma dos {n} números é {r}")
