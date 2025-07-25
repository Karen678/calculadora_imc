def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def menu():
    while True:
        print("\n=== Calculadora de IMC ===")
        print("1. Calcular IMC")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                peso = float(input("Introduce tu peso en kg: "))
                estatura = float(input("Introduce tu estatura en metros: "))
                imc = calcular_imc(peso, estatura)
                clasificacion = clasificar_imc(imc)
                print(f"\nTu IMC es: {imc:.2f}")
                print(f"Clasificación: {clasificacion}")
            except ValueError:
                print("Por favor, introduce valores válidos.")
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
