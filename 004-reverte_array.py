# Reverte os valores de uma matriz numérica
# 23/12/2025

def reverse_list(numbers:list[int]):
    lenght = len(numbers)
    print(f"\nO tamanho da lista é: {lenght}")
    for i in range(int(lenght / 2)):
        temp = numbers[i]
        print(f"temp: {temp} -> numbers[{i}]: {numbers[i]}")
        print(f"numbers[{i}]: {i} = numbers[{lenght - i - 1}]: {numbers[lenght - i -1]}")
        numbers[i] = numbers[lenght - i - 1]
        print(f"numbers[{lenght - i - 1}]: {numbers[lenght - i - 1]} = temp: {temp}")
        numbers[lenght - i - 1] = temp

if __name__ == '__main__':
    test_array = [1,2,3,4,5,6,7,8,9]
    print("Lista normal")
    print(test_array)
    reverse_list(test_array)
    print("\nLista invertida")
    print(test_array)
