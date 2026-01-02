# Transforma temperatura em Celsius para Fahrenheit.
# 23/12/2025

def celsiusToFahrenheit(temp:float) -> float:
    return temp * 1.8 + 32.0

if __name__ == '__main__':
    temperatura = float(input("Digite a temperatura em °C\n--> "))
    fah = celsiusToFahrenheit(temperatura)
    print(f"| {temperatura:.2f}°C | {fah:.2f}°F |")
