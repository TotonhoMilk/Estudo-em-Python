# Conta o número de pontuações na string.
# 22/1/2026

import string


def count_punc(s):
    count = 0
    for char in s:
        if char in string.punctuation:
            count += 1
    return count


if __name__ == "__main__":
    s = "apple, orange, fruits... Anything: grape;"
    r = count_punc(s)
    print(f"O número de pontuações é: {r}")
