# Conta quantas vogais tem em uma string
# 25/12/2025


def count_vowels(str) -> int:
    count = 0
    for letra in str:
        if letra.upper() in "AEIOU":
            count += 1
            print(f"\tA letra '{letra}' é vogal\n\t\tContador = {count}")
    return count


if __name__ == "__main__":
    testStr = "Ola! Tudo bem, por ai!"
    resultado = count_vowels(testStr)
    print(f"A string {testStr} tem {resultado} vogais.")
