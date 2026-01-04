# Valida um tipo especial de string.
# 4/1/2025
#
# Formato válido
# 2DG E4H
# número | letra| número | ESPAÇO | número | letra | número
#   0        1       2        3       4        5       6


def is_valid(str):
    if len(str) != 7:
        return False
    if not str[0].isalpha():
        return False
    if not str[1].isdigit():
        return False
    if not str[2].isalpha():
        return False
    if str[3] != " ":
        return False
    if not str[4].isdigit():
        return False
    if not str[5].isalpha():
        return False
    if not str[6].isdigit():
        return False
    return True


if __name__ == "__main__":
    code = "G3D 5F6"
    if is_valid(code):
        print(f"{code} é valido!")
    else:
        print(f"{code} não é válido!")
