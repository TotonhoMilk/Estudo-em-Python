# Remove vogal de uma palavra.
# 4/1/2026


def is_vowel(letra):
    if letra.lower() in "aeiou":
        return True
    return False


if __name__ == "__main__":
    texto = input("Digite uma palavra -> ")
    tam = len(texto)
    res = ""
    print(f"Tamanho da palavra: {tam} letras")
    for i in range(tam):
        if is_vowel(texto[i]):
            continue
        res += texto[i]
    print(f"Novo tamanho da palavra: {len(res)} letras")
    print(f"Palavra '{texto}' sem vogais é '{res}'")
