# Inverte todas as palavras da string.
# 17/1/2026


def reverse_word(s):
    words = []
    current_word = ""
    for char in s:
        if char not in " .":
            current_word = char + current_word
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
            words.append(char)
    return "".join(words)


if __name__ == "__main__":
    s = "This is the way."
    r = reverse_word(s)
    print(r)

