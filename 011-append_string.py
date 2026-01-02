# Concatena duas strings.
# 25/12/2025


def append_string(s1, s2) -> str:
    return s1 + s2


if __name__ == "__main__":
    str1 = "Primeira "
    str2 = "Segunda"
    p = append_string(str1, str2)
    print(p)
