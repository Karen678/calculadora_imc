
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

if __name__ == "__main__":
    try:
        peso = float(input("Introduce tu peso en kilogramos (kg): "))
        estatura = float(input("Introduce tu estatura en metros (m): "))
        
        if peso <= 0 or estatura <= 0:
            print("El peso y la estatura deben ser mayores que cero.")
        else:
            imc = calcular_imc(peso, estatura)
            clasificacion = clasificar_imc(imc)
            print(f"\nTu IMC es: {imc:.2f}")
            print(f"Clasificación: {clasificacion}")
    except ValueError:
        print("Error: Por favor, introduce valores numéricos válidos.")