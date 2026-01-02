# Determina se o ano é bissexto.
# 25/12/2025


def leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


if __name__ == "__main__":
    ano = int(input("Digite o ano\n--> "))
    if leap_year(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
