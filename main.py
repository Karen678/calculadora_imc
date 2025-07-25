
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
    peso = float(input("Introduce tu peso en kg: "))
    estatura = float(input("Introduce tu estatura en metros: "))
    
    imc = calcular_imc(peso, estatura)
    clasificacion = clasificar_imc(imc)
    
    print(f"Tu IMC es: {imc:.2f}")
    print(f"Clasificación: {clasificacion}")