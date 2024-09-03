# Define función para calcular factorial
# Factorial será el resultado de la multiplicación por todos sus numeros anteriores mayor a 0 e imprime resultado
def calculate_factorial(factorial):
    counter = factorial - 1

    while counter > 0:
        factorial *= counter
        counter -= 1
    
    print(factorial)

# Define función para obtener número al cual se le calculará el factorial     
def get_number():
    factorial = int(input("Ingrese un número para calcular su factorial: "))
    calculate_factorial(factorial)

# Agrega convención
if __name__ == "__main__":
    get_number()