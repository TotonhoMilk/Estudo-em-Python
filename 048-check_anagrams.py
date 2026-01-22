# Confere se duas strings são anagramas.
# 22/1/2026


def is_anagram(s1, s2):
    s1wc = [0] * 26
    s2wc = [0] * 26
    for char in s1:
        lower = ord(char.lower())
        print(f"s1: {char} | lower: {lower} | lower - 'a': {lower - ord('a')}")
        s1wc[lower - ord("a")] += 1
    print("| s1 ==> ", end="")
    print(s1wc)
    for char in s2:
        lower = ord(char.lower())
        print(f"s2: {char} | lower: {lower} | lower - 'a': {lower - ord('a')}")
        s2wc[lower - ord("a")] += 1
    print("| s2 ==> ", end="")
    print(s2wc)
    for i in range(26):
        if s1wc[i] != s2wc[i]:
            return False
    return True


if __name__ == "__main__":
    s1 = "Listen"
    s2 = "Silent"
    if is_anagram(s1, s2):
        print("Anagram!")
    else:
        print("Not anagram!")
