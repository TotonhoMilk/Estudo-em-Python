# Verifica se a string é um palíndromo
# 23/12/2025

def checkPalindrome(str) -> bool:
    lenght = len(str)
    print(f"O tamanho da string é: {lenght}")
    for i in range(int(lenght / 2)):
        print(f"str[{i}]: {str[i]} == str[{lenght-i-1}]: {str[lenght-i-1]}")
        if str[i] != str[lenght - i - 1]:
            print(f"\tFalso!\n\tstr[{i}]: {str[i]} == str[{lenght-i-1}]: {str[lenght-i-1]}")
            return False
    return True

if __name__ == '__main__':
    s = input("Digite a palavra:\n--> ")
    if  checkPalindrome(s):
        print(f"A palavra {s} é palíndromo.")
    else:
        print(f"A palavra {s} não é palíndromo.")
