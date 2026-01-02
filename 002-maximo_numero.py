# Acha o maior número em um test_array
# 23/12/2025

def find_max(numbers:list[int]) ->int:
    max_number = numbers[0]
    for num in numbers:
        print(f"max = {max_number} < {num}")
        if max_number < num:
            max_number = num
            print(f"Verdadeiro\n\tNovo valor de max = {num}")
    return max_number

if __name__ == "__main__":
    test_array = [2,6,4,3,4,8,1,4,3,7]
    maximum = find_max(test_array)
    print(f"Maior número: {maximum}")
