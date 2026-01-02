# Conta ocorrência de um palavra em uma string.
# 26/12/2025


def count_words(string: str, word: str) -> int:
    slen = len(string)
    wlen = len(word)
    end = slen - wlen + 1
    count = 0
    for i in range(end):
        find_word = True
        for j in range(wlen):
            if word[j] != string[i + j]:
                find_word = False
                break
        if find_word:
            count += 1
    return count


if __name__ == "__main__":
    s = "eu sou muito coisado, eu, sou, eu sim."
    w = "eu"
    print(s)
    print(f"A palavra '{w}' apareceu {count_words(s, w)} vezes.")
